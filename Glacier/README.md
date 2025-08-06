# Esports News Summarizer

## Overview
Automated platform to fetch, classify, and summarize esports news in real-time, with a modular agent-based architecture and Streamlit dashboard.

## Features
- Automated news fetching (Tavily API, RSS, scraping)
- Intelligent classification (game, type, region)
- AI summarization (OpenAI, HuggingFace)
- QA/admin review
- Streamlit dashboard and FastAPI API
- MongoDB Atlas storage

## Setup
1. Clone the repo and `cd Glacier`
2. Create a `.env` file (see `.env.example`):
   - `MONGODB_URI=...`
   - `OPENAI_API_KEY=...`
   - `TAVILY_API_KEY=...`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit dashboard:
   ```bash
   streamlit run ui/dashboard.py
   ```
5. Run the FastAPI server:
   ```bash
   uvicorn api.main:app --reload
   ```

## Project Structure
- `agents/` - Modular agents for fetching, classifying, summarizing, formatting, QA
- `data/` - Data models (Pydantic)
- `db/` - MongoDB connection and deduplication
- `ui/` - Streamlit dashboard
- `api/` - FastAPI endpoints

## License
MIT