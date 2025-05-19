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
<<<<<<< HEAD
3. Add your `mochi ops.json` (Google service account key) to the root folder (refer to Gsheets API instructions below)
4. In the terminal, navigate to the path where this repo was cloned. Then input this: streamlit run mood.py
=======
3. Add your 'credentials.json` (Google service account key) to the root folder (refer to Gsheets API instructions below)
4. Run the app:
>>>>>>> 48d1fcf (second commit)


## G Sheets API Setup

1. Enable the **Google Sheets API** on your GCP project.
2. Create a **service account** and generate a JSON key file.
3. Rename the downloaded key to `credentials.json` and place it in the folder of this project. 
4. Share your target Google Sheet with your service account's email address (as an **Editor**).
