import requests
import os
import json
import streamlit as st

def searchPeople(data):
    
    url = st.secrets["SEARCH_URL"]

    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'X-Api-Key': os.getenv("APOLLO_API_KEY")
    }

    response = requests.request("POST", url, headers=headers, json=data)
    return response.json()

def writeToFile(data, filename = "response"):
    with open(f'{filename}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)  