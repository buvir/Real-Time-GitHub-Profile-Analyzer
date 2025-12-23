import streamlit as st
import httpx
import plotly.express as px
import asyncio

# --- BACKEND LOGIC ---
async def fetch_github_data(username):
    # Note: For public data, a token isn't strictly required for REST, 
    # but GraphQL requires a Personal Access Token (PAT).
    # If you don't have a token, we fallback to 'Top Starred' repos.
    
    GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
    # To get REAL pinned repos, you need a token in your Streamlit Secrets
    token = st.secrets.get("GITHUB_TOKEN") 
    
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    # GraphQL Query for Pinned Items
    query = """
    query($login: String!) {
      user(login: $login) {
        pinnedItems(first: 6, types: REPOSITORY) {
          nodes {
            ... on Repository {
              name
              description
              url
              stargazerCount
              forkCount
              primaryLanguage { name }
            }
          }
        }
        repositories(first: 100, ownerAffiliations: OWNER) {
          totalCount
          nodes {
            primaryLanguage { name }
          }
        }
        avatarUrl
        name
        bio
        location
      }
    }
    """

    async with httpx.AsyncClient() as client:
        if token:
            # Try GraphQL for Pinned Repos
            resp = await client.post(GITHUB_GRAPHQL_URL, json={"query": query, "variables": {"login": username}}, headers=headers)
            if resp.status_code == 200:
                raw_data = resp.json().get("data", {}).get("user")
                if raw_data:
                    # Parse Languages for the chart
                    langs = {}
                    for r in raw_data['repositories']['nodes']:
                        l = r.get('primaryLanguage')
                        if l:
                            langs[l['name']] = langs.get(l['name'], 0) + 1
                    
                    return {
                        "profile": raw_data,
                        "language_distribution": langs,
                        "total_repos": raw_data['repositories']['totalCount'],
                        "pinned_repos": raw_data['pinnedItems']['nodes']
                    }

        # FALLBACK: If no token or GraphQL fails, use REST (Top Starred instead of Pinned)
        rest_url = f"https://api.github.com/users/{username}"
        user_resp = await client.get(rest_url)
        repo_resp = await client.get(f"{rest_url}/repos?per_page=100") # Pagination fix
        
        if user_resp.status_code == 200:
            u = user_resp.json()
            r_list = repo_resp.json()
            langs = {}
            for r in r_list:
                l = r.get('language')
                if l: langs[l] = langs.get(l, 0) + 1
            
            return {
                "profile": {"avatarUrl": u['avatar_url'], "name": u['name'], "bio": u['bio'], "location": u['location']},
                "language_distribution": langs,
                "total_repos": u['public_repos'],
                "pinned_repos": sorted(r_list, key=lambda x: x['stargazers_count'], reverse=True)[:6]
            }
    return None

# --- UI CODE ---
st.set_page_config(page_title="GitHub Analyzer", layout="wide")
st.title("🚀 GitHub Profile Analyzer")

username = st.text_input("Enter GitHub Username", "octocat")

if st.button("Analyze"):
    data = asyncio.run(fetch_github_data(username))
    if data:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(data['profile']['avatarUrl'], width=150)
            st.header(data['profile']['name'] or username)
            st.metric("Total Repositories", data['total_repos'])
        
        with col2:
            fig = px.pie(values=list(data['language_distribution'].values()), 
                         names=list(data['language_distribution'].keys()), title="Tech Stack")
            st.plotly_chart(fig)

        st.subheader("📌 Pinned / Featured Repositories")
        cols = st.columns(3)
        for i, repo in enumerate(data['pinned_repos']):
            with cols[i % 3]:
                st.info(f"**[{repo.get('name')}]({repo.get('url') or repo.get('html_url')})**\n\n{repo.get('description') or 'No description'}")
