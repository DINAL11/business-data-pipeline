import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df['amount'] = df['amount'].round(2)
        df['date'] = pd.to_datetime(df['date'])
        print("[Transform] Cleaned and formatted data")
        return df
    except Exception as e:
        print(f"[Transform] Error transforming data: {e}")
        return df
