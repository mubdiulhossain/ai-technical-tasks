from pathlib import Path
import faiss
from config import INDEX_DIM, CHUNK_SIZE, K_RETRIEVE
from llm import embed_model

index = faiss.IndexFlatL2(INDEX_DIM)
metadatas = []

def load_website_texts(folder="website_texts"):
    texts = []
    p = Path(folder)
    for f in p.glob("*.txt"):
        text = f.read_text(encoding="utf-8").strip()
        texts.append((f.name, text))
    return texts

def chunk_text(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def build_index():
    global metadatas, index
    metadatas = []
    index.reset()
    texts = load_website_texts()
    all_chunks = []
    for fname, text in texts:
        for c in chunk_text(text):
            all_chunks.append((fname, c))
    if not all_chunks:
        return
    embeddings = embed_model.encode([c for _,c in all_chunks], show_progress_bar=True)
    index.add(embeddings.astype("float32"))
    metadatas = [{"source": s, "text": c} for s,c in all_chunks]

def retrieve(query, k=K_RETRIEVE):
    if len(metadatas) == 0:
        return [""]
    q_emb = embed_model.encode([query]).astype("float32")
    D, I = index.search(q_emb, k)
    results = []
    for idx in I[0]:
        if idx < len(metadatas):
            results.append(metadatas[idx]["text"])
    return results
