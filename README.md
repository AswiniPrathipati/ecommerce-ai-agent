# ecommerce-ai-agent

#  Ecommerce AI Agent (Internship Assignment for Anarx.ai)

This project builds an AI agent that answers e-commerce data questions using Gemini 2.5, FastAPI, and SQLite.

##  Features

- Accepts user questions via API
- Converts them into SQL queries using Gemini 2.5
- Executes query on SQLite database
- Returns clean, readable results

##  Project Structure

- `data_loader.py` — Loads CSVs into SQLite
- `gemini_query.py` — LLM → SQL conversion using Gemini API
- `main.py` — FastAPI backend
- `.env` — Stores your API Key
- `*.csv` — Provided datasets

##  How to Run

1. Clone the repo and navigate into it
2. Create `.env` file with your Gemini API key
3. Place the 3 CSV files in the root folder
4. Run:

```bash
pip install -r requirements.txt
python data_loader.py
uvicorn main:app --reload
