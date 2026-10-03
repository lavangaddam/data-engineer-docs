
from pathlib import Path
import pandas as pd

# Define file paths
input_path = Path("data/raw/olist_orders_dataset.csv")
output_path = Path("data/processed/orders_cleaned.csv")

# Load the original dataset
orders = pd.read_csv(input_path)

print("--- Original Dataset ---")
print("Shape:", orders.shape)

# Standardize text columns
orders["order_id"] = orders["order_id"].str.strip()
orders["customer_id"] = orders["customer_id"].str.strip()
orders["order_status"] = orders["order_status"].str.strip().str.lower()

# Convert date columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")

# Check for missing primary identifiers
if orders["order_id"].isna().any():
    raise ValueError("Some orders have missing order IDs.")

# Check for duplicate order IDs
duplicate_count = orders["order_id"].duplicated().sum()
print("Duplicate order IDs:", duplicate_count)

if duplicate_count > 0:
    raise ValueError("Duplicate order IDs found. Review before removing them.")

# Check missing values
print("\n--- Missing Values ---")
print(orders.isna().sum())

# Preserve missing timestamps because they may be valid
# for canceled, processing, or other incomplete orders.

# Create output directory if it doesn't exist
output_path.parent.mkdir(parents=True, exist_ok=True)

# Save cleaned dataset
orders.to_csv(output_path, index=False)

print("\n--- Cleaning Complete ---")
print("Cleaned dataset shape:", orders.shape)
print("Saved to:", output_path)