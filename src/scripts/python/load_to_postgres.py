from pathlib import Path
import os

import pandas as pd
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parents[3]
INPUT_FILE = BASE_DIR / "data" / "processed" / "orders_transformed.csv"

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set. "
        "Configure your PostgreSQL connection first."
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
