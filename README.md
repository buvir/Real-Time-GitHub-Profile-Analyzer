🚀 Real-Time GitHub Profile Analyzer
A full-stack data visualization dashboard that provides deep insights into any GitHub profile. This project showcases the ability to handle asynchronous API calls, complex data visualization, and automated CI/CD pipelines.

🔗 Live Demo

✨ Features
Real-Time Analytics: Fetches live data directly from the GitHub API using httpx and asyncio.

Comprehensive Repo Scan: Implements pagination to accurately track users with 40+ repositories.

Tech Stack Visualization: Dynamic Plotly charts showing the distribution of languages across all projects.

Featured Repositories: Automatically identifies and highlights Pinned/Top repositories with interactive cards.

Modern UI: Clean, responsive dashboard built with Streamlit.

🛠️ Tech Stack
Frontend: Streamlit (Python-based Web Framework)

Backend: Python 3.11 with Asyncio

Data Fetching: Httpx (Asynchronous HTTP Client)

Visualization: Plotly Express

CI/CD: GitHub Actions (Automated Testing & Smoke Tests)

Deployment: Streamlit Community Cloud

⚙️ CI/CD Workflow
This project utilizes Continuous Integration and Continuous Deployment via GitHub Actions:

Code Quality Check: Every push triggers a suite of tests to verify API connectivity and logic.

Smoke Testing: Automated checks ensure the Streamlit app starts correctly before going live.

Auto-Deploy: Once tests pass, the live dashboard is instantly updated on Streamlit Cloud.

🚀 Installation & Local Setup
Clone the repository:

Bash

git clone https://github.com/YOUR_USERNAME/Real-Time-GitHub-Profile-Analyzer.git
cd Real-Time-GitHub-Profile-Analyzer
Create and activate a virtual environment:

Bash

python -m venv venv
.\venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Run the application:

Bash

streamlit run app.py
📸 Screenshots
![Streamlit_app](screenshot.png)

## Streamlit LInk
```
https://real-time-app-profile-analyzer.streamlit.app/
```

📂Project Structure

github-analyzer/

├── .github/workflows/

│   └── pipeline.yml       # The CI/CD engine
├── tests/
│   └── test_logic.py      # Automated tests

├── app.py                 # Your main code (Combined)

├── requirements.txt       # Streamlit, httpx, plotly, pytest

└── README.md

