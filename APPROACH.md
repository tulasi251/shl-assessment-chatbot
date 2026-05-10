# SHL Conversational Assessment Recommender

## Overview

This project is a conversational recommendation agent built using FastAPI. The system helps recruiters and hiring managers identify relevant SHL assessments through multi-turn conversations.

The agent supports:
- Clarification for vague queries
- Assessment recommendations
- Recommendation refinement
- Assessment comparison
- Off-topic refusal

The API is fully stateless and follows the schema defined in the assignment.

---

# Tech Stack

- FastAPI
- Python
- BeautifulSoup
- Requests
- Render (deployment)
- GitHub

---

# System Design

The system consists of four major components:

1. Catalog Scraper
2. Conversation Processing
3. Recommendation Engine
4. FastAPI Service

---

# Catalog Retrieval

The SHL product catalog was scraped using BeautifulSoup and Requests.

Relevant assessment URLs and names were extracted and stored locally in `catalog.json`.

Only SHL catalog URLs are returned by the recommendation engine to prevent hallucinations.

---

# Recommendation Logic

The recommendation system uses keyword-based scoring.

The system:
- combines all user messages
- detects technical and personality requirements
- scores catalog entries
- removes duplicates
- returns top recommendations

The system also supports:
- refinement requests
- comparison questions
- clarification flows

---

# Conversation Handling

The API is stateless.

Each `/chat` request receives the full conversation history.

The agent processes all user messages together to maintain conversational context without storing server-side state.

---

# Guardrails

The agent refuses:
- legal advice
- politics
- unrelated topics
- prompt-injection style off-topic requests

This keeps the system scoped strictly to SHL assessment recommendations.

---

# Evaluation Approach

The system was tested against:
- vague user prompts
- multi-turn conversations
- refinement requests
- comparison requests
- off-topic requests

The API schema was validated using FastAPI Swagger documentation.

---

# Challenges

Some challenges encountered:
- handling multi-turn context cleanly
- avoiding duplicate recommendations
- maintaining schema compliance
- deployment debugging on Render

---

# Future Improvements

Potential improvements:
- semantic search using embeddings
- vector database integration
- LLM-powered retrieval
- better ranking algorithms
- dynamic test type classification

---

# Deployment

The project is deployed publicly on Render.

API endpoints:
- `/health`
- `/chat`

Deployment URL:
https://shl-assessment-chatbot.onrender.com