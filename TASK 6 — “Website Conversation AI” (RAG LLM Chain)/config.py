MODEL_PATH = "models/Phi-3-mini-4k-instruct-q4.gguf"
INDEX_DIM = 384
CHUNK_SIZE = 300
K_RETRIEVE = 3
SYSTEM_PROMPT = """You are an SDR (sales development rep). Be helpful, concise, not pushy. Use retrieved website info to answer. At the end, summarize answers and produce a JSON lead object."""
QUAL_QS = [
    "Can I get your full name?",
    "What's your company or organization?",
    "What's your main goal or budget range for this product/service?"
]
