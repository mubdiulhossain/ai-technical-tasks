# Website Conversation AI (RAG / LLM Chain)

## Objective

Test your conversational AI orchestration.

## Description

This project implements a small chatbot workflow that:

* Greets the visitor
* Asks 3 qualification questions (name, company, goal/budget)
* Summarizes the answers
* Outputs a structured JSON lead object
* Maintains the persona of a helpful SDR

---

## Setup Instructions

### 1. Installing the packages

```bash
pip install -r requirements.txt
```

### 2. Download LLM model

Download the Phi-3-mini-4k-instruct-q4.gguf model and place in `models/`:

```bash
pip install huggingface-hub
```

```bash
huggingface-cli login #requires API token
```

```bash
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf     --include "Phi-3-mini-4k-instruct-q4.gguf"     --local-dir models
```

---

## Running the App

```bash
python app.py
```

* Flask server runs at: `http://127.0.0.1:8787`
* Endpoints:

  * `/start` (POST) — Start a session
  * `/message` (POST) — Send user messages
  * `/lead` (GET) — Retrieve JSON lead object

---

## API Flow (using curl)

### Start session

```bash
curl -X POST http://127.0.0.1:8787/start \
-H "Content-Type: application/json" \
-d '{"session_id":"s1"}'
```

API Reply:

```json
{
    "reply": "Hi — I'm the SDR for Betopia. Quick 3 questions so I can help: 1) your name, 2) company, 3) main goal or budget. Ready?",
    "session_id": "s1"
}
```

### 3-step qualification conversation

```bash
curl -X POST http://127.0.0.1:8787/message -H "Content-Type: application/json" -d '{"session_id":"s1","text":"Alice Tan"}'
curl -X POST http://127.0.0.1:8787/message -H "Content-Type: application/json" -d '{"session_id":"s1","text":"Boogle"}'
curl -X POST http://127.0.0.1:8787/message -H "Content-Type: application/json" -d '{"session_id":"s1","text":"We want to explore fintech integration. Budget around 10k."}'
```

### Confirmation from API

```json
{
    "lead": {
        "company": "Boogle",
        "goal_or_budget": "We want to explore fintech integration. Budget around 10k.",
        "name": "Alice Tan",
        "notes": "",
        "source": "website_chat"
    },
    "reply": "Got it. Name: Alice Tan. Company: Boogle. Goal/Budget: We want to explore fintech integration. Budget around 10k.. I'll save that. How can I help further?"
}
```

### Retrieve JSON lead

```bash
curl -X GET "http://127.0.0.1:8787/lead?session_id=s1"
```

**Sample JSON lead object**

```json
{
    "lead": {
        "company": "Boogle",
        "goal_or_budget": "We want to explore fintech integration. Budget around 10k.",
        "name": "Alice Tan",
        "notes": "Alice Tan from Boogle is interested in exploring fintech integration with a budget of approximately $10k.\n\nHere's the corresponding JSON lead object:\n\n{\n  \"name\": \"Alice Tan\",\n  \"company\": \"Boogle\",\n  \"goal\": \"explore fintech integration\",\n  \"budget\": \"$10k\"\n}\n\nBased on the provided information, a short sales note could be:\n\nDear Alice Tan,\n\nThank you for considering our services to explore fintech integration for Boogle. With a budget of around $10k, we believe we can provide you with the solutions you need to achieve your goals.\n\nPlease let us know a convenient time for a call or meeting to discuss this further.\n\nBest regards,\n[Your Name]\n[Your Company]\n\nIf you have any specific requirements or questions, feel free to share them with us.\n\nJSON lead object:\n\n{\n  \"name\": \"Alice Tan\",\n  \"company\": \"Boogle\",\n  \"goal\": \"explore fintech integration\",\n  \"budget\": \"$10k\",\n  \"sales",
        "source": "website_chat"
    }
}
```

---

## Notes

* `.gguf` model files is not uploaded to GitHub.  Evaluators should download them using instructions above.