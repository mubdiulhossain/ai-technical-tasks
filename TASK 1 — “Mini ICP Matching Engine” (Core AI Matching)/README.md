# Mini ICP Matching Engine (Core AI Matching)

### Background

This project implements a simplified version of an ICP (Ideal Customer Profile) similarity engine used in an AI Lead Generator.

- **Task:** “Mini ICP Matching Engine” (Core AI Matching)  
- **Environment:** All steps are implemented and documented in the provided Jupyter notebook, including:
  - Converting company descriptions and ICP into embeddings
  - Computing similarity scores
  - Ranking companies from best to worst match
  - Generating JSON output with company name, similarity score, and explanation (refer to [`results.json`](./results.json))
  - Evaluation and sample results

- **Requirements:** See `requirements.txt` for the list of dependencies.

### Scaling for Millions of Companies

To scale the ICP (Ideal Customer Profile) matching engine for millions of companies, the following strategies can be applied:

#### 1. Precomputing Embeddings
Instead of computing embeddings on the fly, embeddings can be precomputed and stored in a database or vector store, such as:
- **FAISS**
- **Pinecone**
- **Weaviate**, etc.  

This approach reduces runtime computation and speeds up similarity searches.

#### 2. Similarity Search with Vector Database
Use approximate nearest neighbor (ANN) search provided by vector databases.  
Benefits:
- Enables sub-second retrieval
- Efficient for millions of embeddings

#### 3. Indexing and Sharding
- **Indexing** embeddings improves ANN query performance.
- **Sharding** data across multiple nodes allows horizontal scaling for massive datasets.

### Notes on Dataset
- The dataset used for demonstration was **synthetic** and may not accurately reflect real-world company descriptions.
- Real-world data is usually more varied and contains richer text, likely producing better matches.

---

**Author:** Mubdiul Hossain
