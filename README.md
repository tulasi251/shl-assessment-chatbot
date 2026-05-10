# SHL Conversational Assessment Recommender

A conversational AI-based recommendation system built for the SHL AI Intern take-home assignment.

The system helps recruiters and hiring managers discover relevant SHL assessments through multi-turn conversations.

---

# Features

- Clarification for vague hiring requests
- SHL assessment recommendations
- Recommendation refinement
- Assessment comparison
- Off-topic refusal handling
- Stateless FastAPI API
- Public deployment on Render

---

# Tech Stack

- Python
- FastAPI
- BeautifulSoup
- Requests
- GitHub
- Render

---

# API Endpoints

## Health Check

GET `/health`

Example response:

```json
{
  "status": "ok"
}
```

---

## Chat Endpoint

POST `/chat`

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java developer with personality fit"
    }
  ]
}
```

Example response:

```json
{
  "reply": "Here are some recommended SHL assessments.",
  "recommendations": [
    {
      "name": "Assessment Name",
      "url": "https://www.shl.com/...",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
```

---

# Project Structure

```bash
├── app.py
├── scraper.py
├── catalog.json
├── requirements.txt
├── render.yaml
├── APPROACH.md
└── README.md
```

---

# Deployment

## Health Endpoint

https://shl-assessment-chatbot.onrender.com/health

Returns:

```json
{"status":"ok"}
```

---

## Swagger API Documentation

https://shl-assessment-chatbot.onrender.com/docs
---

# How It Works

1. SHL catalog is scraped using BeautifulSoup
2. Assessment names and URLs are stored in `catalog.json`
3. User conversation history is processed
4. The system detects:
   - technical requirements
   - personality requirements
   - refinement requests
   - comparison requests
5. Recommendations are ranked and returned

---

# Supported Behaviors

- Clarification Questions
- Recommendations
- Refinement Handling
- Comparison Handling
- Off-topic Refusal

---

# Future Improvements

- Embedding-based semantic search
- Vector database integration
- LLM-powered ranking
- Better recommendation scoring
- Dynamic assessment classification

---

# Author

Gangarapu Tulasikrishna