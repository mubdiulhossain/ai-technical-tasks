import numpy as np
import pandas as pd

def generate_dataset(n_samples=3000, save_csv=False, csv_path="synthetic_leads.csv", random_seed=42):
    """
    Generates a synthetic lead scoring dataset.
    
    Args:
        n_samples (int): Number of leads to generate.
        save_csv (bool): Whether to save the dataset as a CSV file.
        csv_path (str): Path to save CSV if save_csv=True.
        random_seed (int): Seed for reproducibility.
        
    Returns:
        pd.DataFrame: Synthetic dataset.
    """
    np.random.seed(random_seed)

    company_size = np.random.randint(1, 5001, n_samples)

    industries = ['Finance', 'Retail', 'Tech', 'Health', 'Education']
    industry = np.random.choice(industries, n_samples)

    tech_keywords = ['Python', 'Java', 'Kotlin', 'React', 'AWS', 'SQL', 'NodeJS']
    tech_stack_keywords = [
        ', '.join(np.random.choice(tech_keywords, size=np.random.randint(1,4), replace=False))
        for _ in range(n_samples)
    ]

    page_visits = np.random.randint(1, 101, n_samples)

    intent_signal = np.round(np.random.rand(n_samples), 2)

    historical_conversion_rate = np.round(np.random.rand(n_samples), 2)

    converted = ((page_visits + intent_signal*50 + historical_conversion_rate*50) > 70).astype(int)

    df = pd.DataFrame({
        'company_size': company_size,
        'industry': industry,
        'tech_stack_keywords': tech_stack_keywords,
        'page_visits': page_visits,
        'intent_signal': intent_signal,
        'historical_conversion_rate': historical_conversion_rate,
        'converted': converted
    })

    if save_csv:
        df.to_csv(csv_path, index=False)
        print(f"Dataset saved to {csv_path}")

    return df
