

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

# Use the project root as the current working directory
BASE_DIR = Path.cwd()
INPUT_FILE = BASE_DIR / "data" / "processed" / "orders_transformed.csv"

DATABASE_URL = (
    "postgresql+psycopg2://lavankumatgaddam@localhost:5432/olist_db"
)

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"CSV file not found: {INPUT_FILE}")

engine = create_engine(DATABASE_URL)

try:
    orders = pd.read_csv(INPUT_FILE)
    print(f"Loaded CSV: {orders.shape[0]} rows, {orders.shape[1]} columns")

    orders.to_sql(
        "orders",
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    with engine.connect() as connection:
        count = connection.execute(
            text("SELECT COUNT(*) FROM orders")
        ).scalar()

    print(f"Successfully loaded {count} rows into PostgreSQL!")

finally:
    engine.dispose() 
SELECT
    order_status,
    COUNT(*) AS total_orders 
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;
