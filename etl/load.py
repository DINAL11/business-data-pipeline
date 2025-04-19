import sqlite3
import pandas as pd

def load_data(df: pd.DataFrame, db_name: str = "sales.db"):
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql("sales", conn, if_exists="replace", index=False)
        print(f"[Load] Loaded {len(df)} rows into {db_name}")
        conn.close()
    except Exception as e:
        print(f"[Load] Error loading to DB: {e}")
