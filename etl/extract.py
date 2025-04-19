import pandas as pd

def extract_data(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
        print(f"[Extract] Loaded {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        print(f"[Extract] Error loading data: {e}")
        return pd.DataFrame()
