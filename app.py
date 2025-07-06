import gradio as gr
import networkx as nx
import pandas as pd
from transformers import pipeline


metro = pd.read_csv('M4_Estaciones_FULL.csv', sep=';')
G= nx.Graph()

for _, row in metro.iterrows():
    G.add_edge(
        row['From_Station'],
        row['To_Station'],
        line=row['line_from'],
        direction=['Direction_head'],
        is_tranfer=['is_transfer']        
    )

ner_pipeline=pipeline('ner',model='dslim/bert-base-NER', grouped_entities=True)   #grouped_entities call groups together tokens that belong to the same entity

def find_route(G, origin, destination):
    try:
        path= nx.shortest_path(G, source=origin, target=destination)

        output=[]
        for i in range(len(path)-1):
            from_station=path[i]
            to_station=path[i+1]

            data= G.get_edge_data(from_station, to_station)  ### we need to do this, so we obtained the line of the metro
            line=data.get('line','N/A')
            head=data.get('Direction_head','N/A')
            step=f'{from_station} -> {to_station} (Line {line} -> {head})'
            output.append(step)

        return '\n'.join(output)
    except nx.NetworkXNoPath:
        return f"No route found from {origin} to {destination}"
    except nx.NodeNotFound as e:
        return str(e)

def extract_stations(text):
    ner_results= ner_pipeline(text)
    stations=[ent['word'] for ent in ner_results if ent['entity_group'] == 'LOC']
    return stations    

def chat_bot(user_input, history):
    user_input = user_input.title()
    stations=extract_stations(user_input)
    if len(stations) <2:
        return 'Please mention both origin and destination station'
    return find_route(G, stations[0], stations[1])


demo = gr.ChatInterface(chat_bot)
demo.launch()
