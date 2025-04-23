import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data():
    conn = sqlite3.connect("sales.db")
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def visualize_sales_trends(df):
    # Group by date and sum the amount
    df['date'] = pd.to_datetime(df['date'])
    df_daily = df.groupby('date')['amount'].sum().reset_index()
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_daily['date'], df_daily['amount'], marker='o', linestyle='-', color='b')
    plt.title("Sales Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def visualize_sales_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['amount'], kde=True, bins=30, color='green')
    plt.title("Sales Distribution (Amount)")
    plt.xlabel("Transaction Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def visualize_sales_summary(df):
    df_daily = df.groupby('date')['amount'].sum().reset_index()
    df_daily.set_index('date', inplace=True)
    
    plt.figure(figsize=(10, 6))
    df_daily.plot(kind='bar', legend=False)
    plt.title("Total Sales Per Day")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = fetch_data()
    visualize_sales_trends(df)
    visualize_sales_distribution(df)
    visualize_sales_summary(df)
