from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="GitHub Profile Analyzer API")

GITHUB_API_URL = "https://api.github.com/users"

@app.get("/analyze/{username}")
async def analyze_user(username: str):
    async with httpx.AsyncClient() as client:
        # Fetch user profile
        user_resp = await client.get(f"{GITHUB_API_URL}/{username}")
        if user_resp.status_code != 200:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Fetch user repos
        repo_resp = await client.get(f"{GITHUB_API_URL}/{username}/repos")
        repos = repo_resp.json()
        
        # Simple Logic: Count languages
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
