import requests
import os
import streamlit as st

def askLyzrAgent(message):
    url = st.secrets["LYZR_URL"]
    api_key = st.secrets["LYZR_API_KEY"]

    if not api_key:
        raise ValueError("No API key set in environment variables")
    
    headers = {
        "accept": "application/json",
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "user_id": st.secrets["LYZR_USER_ID"],
        "agent_id": st.secrets["LYZR_PROSPECT_AGENT_ID"],
        "session_id": st.secrets["LYZR_SESSION_ID"],
        "message": message 
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['response'] 
    else:
        response.raise_for_status()


