import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pandas as pd
import plotly.express as px


#Handling Google sheets authentication here (credit to Tech with Tim on Youtube) 
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
client = gspread.authorize(creds)
sheet_id = "1te-FGjb1zr7WQ9CphIFFSSrzrPap52gmg7BfNCSn9xA"
sheet = client.open_by_key(sheet_id).sheet1

# Streamlit Frontend code
st.title("🧠 Mood Tracker")

moods = {
    "Happy 😊": "😊",
    "Angry 😠": "😠",
    "Okay 😕": "😕",
    "Excited 🎉": "🎉"}

# Created a Streamlit form function 
with st.form("mood_form"):
    mood = st.selectbox("How are you feeling?", list(moods.keys()))
    note = st.text_input("Optional note:")
    submitted = st.form_submit_button("Submit")

    if submitted:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mood_emoji = moods[mood]
        sheet.append_rows([[timestamp, mood_emoji, note]], value_input_option= "RAW")
        st.success("Mood logged successfully!") 

#Everything below here is code related to the bar graph visual

all_records = sheet.get_all_records()
# Convert to DataFrame
df = pd.DataFrame(all_records)

if not df.empty:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    if not df.empty:
        mood_counts = df['Mood'].value_counts().reset_index()
        mood_counts.columns = ['Mood', 'Count']

        #Plot bar chart with Plotly libary
        fig = px.bar(mood_counts, x='Mood', y='Count', title="Mood Counts for Today", text='Count')
        st.plotly_chart(fig)
    else:
        st.info("No moods logged today")
else:
    st.info("No mood data found")