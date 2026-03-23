# frontend/app.py
import streamlit as st
import requests

st.title("DS POC App 🚀")

st.write("Simple frontend connected to FastAPI")

# Inputs
name = st.text_input("Enter your name")
task = st.text_input("Enter a task")

# Button
if st.button("Send Request"):
    url = "http://backend:8000/example/"

    payload = {
        "name": name,
        "task": task
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            result = response.json()["result"]
            st.success("Response received!")
            st.write(result)
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Connection error: {e}")