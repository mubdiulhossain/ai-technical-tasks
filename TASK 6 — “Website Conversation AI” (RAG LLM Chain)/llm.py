from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
from config import MODEL_PATH
import os

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. Please download and place it there."
    )

llm = Llama(model_path=MODEL_PATH, n_ctx=4096, n_threads=6)

def call_llm(system_prompt, user_prompt):
    prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{user_prompt}\n<|assistant|>\n"
    out = llm(prompt, max_tokens=256, temperature=0.4, top_p=0.9, stop=["</s>", "<|user|>"])
    return out["choices"][0]["text"].strip()
