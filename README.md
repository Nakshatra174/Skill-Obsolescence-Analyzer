# 📈 AI-Based Skill Obsolescence Analyzer

A predictive analytics dashboard built with Django that helps tech professionals identify declining skills and pivot to high-growth career paths.

## 🚀 Features
* **Machine Learning Forecasting:** Uses `scikit-learn` (Linear Regression) to predict 2026 job market demand based on historical data.
* **Explainable AI (XAI):** Dynamically generates risk impact scores so users understand *why* a skill is flagged as declining or growing.
* **Live API Integration:** Fetches real-time job posting volumes using Google Jobs Intelligence (with a built-in deterministic mock mode for presentations).
* **Dual-Vector Resume Matcher:** Compares user resumes directly against live Job Descriptions to find critical skill gaps.

## 🛠️ Tech Stack
* **Backend:** Python, Django, SQLite
* **Data Science:** Pandas, NumPy, Scikit-Learn
* **Frontend:** Bootstrap 5, Chart.js, TomSelect

## 💻 Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python manage.py runserver`

*Developed as a final semester MCA project.*FL