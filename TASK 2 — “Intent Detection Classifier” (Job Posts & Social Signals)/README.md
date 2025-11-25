# Intent Detection Classifier (Job Posts & Social Signals)

This project implements a lightweight intent classifier for job posts and social posts.

- **Task:** “Intent Detection Classifier” (Job Posts & Social Signals)  
- **Environment:** All steps are implemented and documented in the provided Jupyter notebook, including:
  - Dataset generation or selection (synthetic or real)
  - Feature engineering and/or prompting strategy
  - Training a classifier to detect intent categories:
    - **High Intent** – e.g., “Looking for HR automation tools”
    - **Medium Intent** – e.g., “Hiring an HR Manager”
    - **Low Intent** – generic but related
    - **No Intent** – irrelevant content
  - Evaluation with ROC/AUC and accuracy metrics
  - Sample outputs and predictions

- **Requirements:** See `requirements.txt` for the list of dependencies.

- **Author:** Mubdiul Hossain



**Short explanation of feature engineering or prompting strategy:**

**Explanation:** Generated synthetic training data using structured templates for each intent class, with variations and added noise. Texts were encoded into embeddings using `SentenceTransformer('all-MiniLM-L6-v2')`, and a `OneVsRestClassifier` with `LogisticRegression` was trained on these embeddings to classify intent.  

**Dataset:** The generated synthetic dataset is based on limited templates. 5-10 sentences were generated per post, containing relevant intent sentences, generic sentences, locations, and noise per post. 
Further randomization or additional template sentences may improve the model’s ability to classify intents more confidently. For best results, training with real-world data would yield the most reliable performance for this intent detection classifier. Hence, generated post are limited to 250 per intent to avoid overfitting.