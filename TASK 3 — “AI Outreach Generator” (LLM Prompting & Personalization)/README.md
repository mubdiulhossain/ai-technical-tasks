# AI Outreach Generator (LLM Prompting & Personalization)

This project implements a personalized sales outreach message generator using LLMs.

## DISCLAIMER

***Due to hardware and API constraint only a small model i.e., "Phi-3-mini-4k-instruct-q4" was used to showcase TASK 3. Other large model would require dedicated system or paid subscriptions for best results.***

* **Task:** “AI Outreach Generator” (LLM Prompting & Personalization)

* **Environment:** All steps are implemented and documented in the provided Jupyter notebook, including:

  * Input preparation:

    * Company profile (industry, size, challenges, website)
    * Persona profile (role, bio, responsibilities)
    * Product description
  * Prompt-based system for generating personalized outreach emails
  * Support for tone variations: Formal / Friendly / Short / Long
  * Prevention of hallucinations
  * Explanation of why the lead is a good match
  * Sample outputs demonstrating personalization

## Setup Instructions

### 1. Installing llama

```bash
pip install llama-cpp-python
```

### 2. Download LLM model

Download the Phi-3-mini-4k-instruct-q4.gguf model and place it in `models/`:

```bash
pip install huggingface-hub
huggingface-cli login # requires API token
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf \
    --include "Phi-3-mini-4k-instruct-q4.gguf" \
    --local-dir models
```

This project implements a personalized sales outreach message generator using LLMs.

- **Task:** “AI Outreach Generator” (LLM Prompting & Personalization)  
- **Notebook:** The Jupyter notebook provides the code which includes the prompt function, model initialization, including:
- Sample outputs demonstrating personalization
- **Requirements:** See `requirements.txt` for the list of dependencies.

### Why this personalization works:

1. The email directly addresses Jane Smith’s role as Head of Operations and aligns with her responsibilities.
2. It acknowledges her 10+ years of experience and focus on efficiency and productivity.
3. The product is clearly connected to her operational goals, showing a strong fit. 
4. To minmize hallucination, invented facts, the prompt is engineered specifically to address those. (although small model like TinyLlama tends to ignore sometimes)
5. The tone is friendly and short, making the message approachable.
6. The content is focused on relevant product benefits, improving readability and engagement.

- **Author:** Mubdiul Hossain
