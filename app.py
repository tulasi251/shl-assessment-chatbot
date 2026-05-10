from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


# Request schema
class ChatRequest(BaseModel):
    messages: list


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    messages = request.messages

    # Combine user conversation
    conversation_text = ""

    for msg in messages:
        if msg["role"] == "user":
            conversation_text += msg["content"].lower() + " "

    # Clarification logic
    vague_words = [
        "assessment",
        "test",
        "hiring",
        "job",
        "developer"
    ]

    if conversation_text.strip() in vague_words:

        return {
            "reply": "What role, seniority level, and skills are you hiring for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Off-topic refusal
    off_topic_words = [
        "salary",
        "legal",
        "law",
        "weather",
        "movie",
        "politics",
        "recipe"
    ]

    for word in off_topic_words:

        if word in conversation_text:

            return {
                "reply": "I can only help with SHL assessment recommendations.",
                "recommendations": [],
                "end_of_conversation": False
            }

    # Comparison feature
    if "difference" in conversation_text or "compare" in conversation_text:

        return {
            "reply": "OPQ is mainly a personality assessment, while GSA focuses more on cognitive and problem-solving abilities.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Detect requirements
    personality_requested = "personality" in conversation_text

    technical_requested = any(
        word in conversation_text
        for word in ["java", "developer", "coding", "programming"]
    )

    recommendations = []

    # Search catalog
    for item in catalog:

        name = item["name"].lower()

        score = 0

        # Match conversation words
        for word in conversation_text.split():

            if len(word) > 3 and word in name:
                score += 1

        # Personality bonus
        if personality_requested:

            personality_words = [
                "personality",
                "behavior",
                "opq"
            ]

            for word in personality_words:

                if word in name:
                    score += 2

        # Technical bonus
        if technical_requested:

            technical_words = [
                "java",
                "developer",
                "programming",
                "coding",
                "technical"
            ]

            for word in technical_words:

                if word in name:
                    score += 2

        # Add relevant results
        if score > 0:

            recommendations.append({
                "name": item["name"],
                "url": item["url"],
                "score": score
            })

    # Remove duplicates
    unique_recommendations = []
    seen = set()

    for item in recommendations:

        if item["url"] not in seen:
            seen.add(item["url"])
            unique_recommendations.append(item)

    # Sort by score
    recommendations = sorted(
        unique_recommendations,
        key=lambda x: x.get("score", 0),
        reverse=True
    )

    recommendations = recommendations[:10]

    # No results
    if len(recommendations) == 0:

        return {
            "reply": "Can you provide more details about the role and skills required?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Final response format
    final_recommendations = []

    for item in recommendations:

        final_recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": "K"
        })

    return {
        "reply": "Here are some recommended SHL assessments.",
        "recommendations": final_recommendations,
        "end_of_conversation": False
    }