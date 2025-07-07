---
title: Madrid Metro Assistant
sdk: gradio
short_description: Chatbot that helps you find routes between Madrid Metro stat
---
# 🚇 Madrid Metro Assistant

A simple chatbot that helps you find routes between Madrid Metro stations — built with 🐍 Python, 🤗 Hugging Face Transformers, 🧠 NetworkX, and 🎨 Gradio!

## 💡 Features

- Natural language input (e.g., *“How do I go from Sol to Tribunal?”*)
- Finds the shortest path across metro lines
- Recognizes station names using a transformer-based NER model
- Fuzzy matching to correct slight typos in station names
- Clean and user-friendly interface in dark mode 🌑

## 🚀 Try it

👉 [Live demo on Hugging Face Spaces](https://huggingface.co/spaces/your_username/chatbot-metro-madrid)

## 🛠️ Tech Stack

- `Gradio` – frontend UI
- `NetworkX` – graph logic + pathfinding
- `Transformers` – for NER (Named Entity Recognition)
- `RapidFuzz` – fuzzy matching for station names
- `Pandas`

## 📁 Files

- `app.py`: Main logic + chatbot function
- `metro_data.csv`: Cleaned dataset of metro connections
- `requirements.txt`: Dependencies

## ❤️ Built by

Victoria

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference