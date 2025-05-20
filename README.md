# 🧠 Mood Tracker App

A simple Streamlit app to log and visualize your daily moods using Google Sheets.

## Features
- Log mood and optional notes
- Store entries in a connected Google Sheet
- Visualize mood trends in a bar chart

## How to Run

1. Clone this repo
2. Install these libraries in your terminal: 
pip install -r requirements.txt
3. Add your 'credentials.json` (Google service account key) to the root folder (refer to Gsheets API instructions below)
4. Go into the file path in your termainal and input: streamlit run mood.py

## G Sheets API Setup

1. Enable the **Google Sheets API** on your GCP project.
2. Create a **service account** and generate a JSON key file.
3. Rename the downloaded key to `credentials.json` and place it in the folder of this project. 
4. Share my Google Sheet with your service account's email address (as an **Editor**).



Link to my [Google Sheet](https://docs.google.com/spreadsheets/d/15-fXuQl3163AsnpNuQv0GypyAcfwtHPZ93MilefjPYk/edit?gid=0#gid=0)
Link to my [Project Walkthrough (Loom)](https://www.loom.com/share/a9acfc01cc0a4e3da73401d06445010f?sid=b5a7cdad-7286-4204-b2a4-5461678f3c83)
