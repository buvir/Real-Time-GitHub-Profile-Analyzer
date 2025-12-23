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

📂Project Structure

github-analyzer/

├── .github/workflows/

├── app.py                # Combined Backend + Frontend logic

├── requirements.txt      # Combined dependencies

├── .gitignore
└── README.md

