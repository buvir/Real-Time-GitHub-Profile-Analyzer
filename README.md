# 🚀 GitHub Profile Analyzer
A Full-Stack application featuring a **FastAPI** backend and **Streamlit** frontend.

## 🛠️ Features
- Real-time data fetching from GitHub REST API.
- Data visualization using **Plotly**.
- Automated **CI/CD** via GitHub Actions.
- Hosted on **Render** and **Streamlit Cloud**.

## 🚦 How to Run Locally
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r backend/requirements.txt`
4. `uvicorn backend.main:app --reload`

## Streamlit_app_LINK:

YOU CAN JUST PASTE THE GITHUB PROFILE NAME AND CLICK ANALYSE AND GET ALL THE PINNED REPOS AND TOTAL REPOS COUNT
```
https://real-time-app-profile-analyzer.streamlit.app/
```


## Screenshot
![Streamlit_app](screenshot.png)


📂Project Structure

github-analyzer/

├── .github/workflows/

│   └── pipeline.yml       # The CI/CD engine
├── tests/
│   └── test_logic.py      # Automated tests

├── app.py                 # Your main code (Combined)

├── requirements.txt       # Streamlit, httpx, plotly, pytest

└── README.md

