
from pathlib import Path
import pandas as pd

# Input and output paths
input_path = Path("data/processed/orders_cleaned.csv")
output_path = Path("data/processed/orders_transformed.csv")

# Load cleaned data
orders = pd.read_csv(input_path)

# Convert timestamps back to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")

# Extract purchase date
orders["purchase_date"] = orders["order_purchase_timestamp"].dt.date

# Calculate actual delivery duration in days
orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Calculate estimated delivery duration in days
orders["estimated_delivery_days"] = (
    orders["order_estimated_delivery_date"]
    - orders["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Calculate delivery delay in days
orders["delivery_delay_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

# Save transformed data
output_path.parent.mkdir(parents=True, exist_ok=True)
orders.to_csv(output_path, index=False)

# Display results
print("--- Transformation Complete ---")
print("Rows:", len(orders))
print("Columns:", len(orders.columns))
print("\nNew columns:")
print([
    "purchase_date",
    "delivery_days",
    "estimated_delivery_days",
    "delivery_delay_days"
])

print("\n--- Sample Transformed Data ---")
print(
    orders[
        [
            "order_id",
            "order_status",
            "purchase_date",
            "delivery_days",
            "estimated_delivery_days",
            "delivery_delay_days"
        ]
    ].head(10)
)

print("\nSaved to:", output_path)