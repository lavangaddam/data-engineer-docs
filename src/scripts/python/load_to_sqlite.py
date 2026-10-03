
from pathlib import Path
import sqlite3
import pandas as pd

# File paths
input_path = Path("data/processed/orders_transformed.csv")
database_path = Path("data/processed/olist.db")

# Create database folder if needed
database_path.parent.mkdir(parents=True, exist_ok=True)

# Load transformed dataset
orders = pd.read_csv(input_path)

# Connect to SQLite database
connection = sqlite3.connect(database_path)

try:
    # Load data into a SQL table
    orders.to_sql(
        "orders",
        connection,
        if_exists="replace",
        index=False
    )

    # Verify the number of records
    result = pd.read_sql_query(
        "SELECT COUNT(*) AS total_orders FROM orders",
        connection
    )

    print("--- Database Load Complete ---")
    print("Database:", database_path)
    print("Table: orders")
    print("Rows loaded:", result.iloc[0]["total_orders"])

    # Preview the data using SQL
    sample = pd.read_sql_query(
        """
        SELECT order_id, order_status, delivery_days,
               delivery_delay_days
        FROM orders
        LIMIT 5
        """,
        connection
    )

    print("\n--- SQL Query Sample ---")
    print(sample)

finally:
    connection.close()