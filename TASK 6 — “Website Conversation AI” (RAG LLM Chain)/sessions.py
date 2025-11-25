SESSIONS = {}

def start_session(session_id):
    SESSIONS[session_id] = {"step": "greet", "answers": []}
    return SESSIONS[session_id]

def get_session(session_id):
    return SESSIONS.setdefault(session_id, {"step":"greet","answers":[]})

def clear_sessions():
    global SESSIONS
    SESSIONS = {}
