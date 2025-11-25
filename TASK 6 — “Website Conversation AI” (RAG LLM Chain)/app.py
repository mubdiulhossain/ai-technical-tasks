#!/usr/bin/env python

from flask import Flask, request, jsonify
from config import SYSTEM_PROMPT, QUAL_QS
from sessions import start_session, get_session
from rag import build_index, retrieve
from llm import call_llm
from sessions import clear_sessions

build_index()

app = Flask(__name__)

@app.route("/start", methods=["POST"])
def start():
    session_id = request.json.get("session_id", "anon")
    start_session(session_id)
    greeting = "Hi — I'm the SDR for Betopia. Quick 3 questions so I can help: 1) your name, 2) company, 3) main goal or budget. Ready?"
    return jsonify({"session_id": session_id, "reply": greeting})

@app.route("/message", methods=["POST"])
def message():
    session_id = request.json.get("session_id", "anon")
    text = request.json.get("text", "")
    session = get_session(session_id)
    step = session["step"]

    if step in ("greet", "q1", "q2"):
        answer_index = 0 if step=="greet" else (1 if step=="q1" else 2)
        session["answers"].append(text.strip())
        if answer_index+1 < len(QUAL_QS):
            session["step"] = "q"+str(answer_index+1)
            next_q = QUAL_QS[answer_index+1]
            return jsonify({"reply": next_q})
        else:
            session["step"] = "done_qual"
            summary = f"Got it. Name: {session['answers'][0]}. Company: {session['answers'][1]}. Goal/Budget: {session['answers'][2]}."
            lead = {
                "name": session["answers"][0],
                "company": session["answers"][1],
                "goal_or_budget": session["answers"][2],
                "source": "website_chat",
                "notes": ""
            }
            session["lead"] = lead
            session["step"] = "chat"
            return jsonify({"reply": f"{summary} I'll save that. How can I help further?", "lead": lead})

    retrieved = retrieve(text)
    context = "\n\n---\n".join(retrieved)
    user_prompt = f"User: {text}\n\nContext:\n{context}\n\nAlso keep persona as helpful SDR and be concise. If user asks for contact, add next steps."
    answer = call_llm(SYSTEM_PROMPT, user_prompt)
    return jsonify({"reply": answer})

@app.route("/lead", methods=["GET"])
def get_lead():
    session_id = request.args.get("session_id","anon")
    session = get_session(session_id)
    lead = session.get("lead", {})
    if lead:
        summary_prompt = f"Summarize the following answers into a short sales note:\nName: {lead['name']}\nCompany: {lead['company']}\nGoal/Budget: {lead['goal_or_budget']}"
        note = call_llm(SYSTEM_PROMPT, summary_prompt)
        lead["notes"] = note
    return jsonify({"lead": lead})

if __name__ == "__main__":
    app.run(port=8787)

@app.route("/clear_sessions", methods=["POST"])
def clear_all_sessions():
    clear_sessions()
    return {"status":"ok", "message":"All sessions cleared"}
