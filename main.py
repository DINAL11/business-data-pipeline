from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    print("[ETL] Starting pipeline")
    df = extract_data("data/sample_sales.csv")
    if not df.empty:
        df = transform_data(df)
        load_data(df)
    print("[ETL] Pipeline finished")

if __name__ == "__main__":
    main()
