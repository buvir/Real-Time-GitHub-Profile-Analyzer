import streamlit as st
import httpx
import plotly.express as px
import asyncio

# --- BACKEND LOGIC (The "FastAPI" part) ---
async def fetch_github_data(username):
    GITHUB_API_URL = "https://api.github.com/users"
    async with httpx.AsyncClient() as client:
        # Fetch user profile
        user_resp = await client.get(f"{GITHUB_API_URL}/{username}")
        if user_resp.status_code != 200:
            return None
        
        # Fetch user repos
        repo_resp = await client.get(f"{GITHUB_API_URL}/{username}/repos")
        repos = repo_resp.json()
        
        # Calculate Language Distribution
        languages = {}
        for repo in repos:
            lang = repo.get("language")
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
        
        return {
            "profile": user_resp.json(),
            "language_distribution": languages,
            "total_repos": len(repos)
        }

# --- FRONTEND UI (The Streamlit part) ---
st.set_page_config(page_title="GitHub Analyzer", layout="wide")

st.title("🚀 Real-Time GitHub Profile Analyzer")
st.markdown("This app analyzes GitHub profiles using Python logic directly.")

username = st.text_input("Enter GitHub Username", "tiangolo")

if st.button("Analyze Profile"):
    with st.spinner(f"Analyzing {username}..."):
        # Running the async function inside Streamlit
        data = asyncio.run(fetch_github_data(username))
        
        if data:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(data['profile']['avatar_url'], width=200)
                st.header(data['profile'].get('name') or username)
                st.info(f"📍 Location: {data['profile'].get('location', 'Not specified')}")
                st.metric("Total Repositories", data['total_repos'])
                st.write(f"📝 Bio: {data['profile'].get('bio', 'No bio available')}")
            
            with col2:
                langs = data['language_distribution']
                if langs:
                    fig = px.pie(
                        values=list(langs.values()), 
                        names=list(langs.keys()), 
                        title="Top Languages Used",
                        hole=0.4
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No language data found for this user.")
        else:
            st.error("User not found! Please check the username.")
