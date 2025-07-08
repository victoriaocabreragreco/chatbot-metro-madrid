---
title: Madrid Metro Assistant
sdk: gradio
short_description: Chatbot that helps you find routes between Madrid Metro stat
---
# 🚇 Madrid Metro Assistant

A simple chatbot that helps you find routes between Madrid Metro stations — built with Python, Hugging Face Transformers (NER), NetworkX, and  Gradio!

## 💡 Features

- Natural language input (e.g., *“How do I go from Sol to Tribunal?”*)
- Finds the shortest path across metro lines
- Recognizes station names using a transformer-based NER model
- Fuzzy matching to correct slight typos in station names
- Clean and user-friendly interface in dark mode 🌑
- At the moment, works better for English input

📷 Key Visuals

Thanks to the fuzzy matching library, the bot can handle misspelled station names

https://github.com/victoriaocabreragreco/chatbot-metro-madrid/blob/main/images/arguelles-quevedo.png

And you don’t need to write station names in capital letters — the bot understands lowercase too!

!(Images/pacifico-lavapies.png)

## 🚀 Try it

👉 [Live demo on Hugging Face Spaces](https://huggingface.co/spaces/your_username/chatbot-metro-madrid)

## 🛠️ Tech Stack

- `Gradio` 
- `NetworkX` 
- `Transformers` 
- `RapidFuzz` 
- `Pandas`


## ❤️ Built by Victoria

