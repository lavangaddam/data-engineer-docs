import pandas as pd
from sqlalchemy import create_engine, text

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2:///olist_db")

# Load customer CSV
file_path = "data/raw/olist_customers_dataset.csv"

df = pd.read_csv(
    file_path,
    dtype={"customer_zip_code_prefix": str}
)

# Load data into PostgreSQL
df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

# Verify the loaded data
with engine.connect() as connection:
    count = connection.execute(
        text("SELECT COUNT(*) FROM customers")
    ).scalar()

    print(f"Successfully loaded {count} customer records.")

    result = connection.execute(
        text("SELECT * FROM customers LIMIT 5")
    )

    for row in result:
        print(row)

engine.dispose()