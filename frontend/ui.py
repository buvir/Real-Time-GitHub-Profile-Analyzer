import streamlit as st
import requests
import plotly.express as px

st.set_page_config(page_title="GitHub Analyzer", layout="wide")

st.title("🚀 Real-Time GitHub Profile Analyzer")
username = st.text_input("Enter GitHub Username", "tiangolo")

# Point this to your Render URL after deployment
BACKEND_URL = "http://localhost:8000" 

if st.button("Analyze"):
    with st.spinner("Fetching data from GitHub..."):
        response = requests.get(f"{BACKEND_URL}/analyze/{username}")
        
        if response.status_code == 200:
            data = response.json()
            
            # Layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(data['profile']['avatar_url'], width=150)
                st.header(data['profile']['name'])
                st.write(data['profile']['bio'])
            
            with col2:
                # Plotly Chart
                langs = data['language_distribution']
                fig = px.pie(values=list(langs.values()), names=list(langs.keys()), title="Tech Stack")
                st.plotly_chart(fig)
        else:
            st.error("User not found!")
