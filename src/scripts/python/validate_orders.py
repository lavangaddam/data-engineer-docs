
import pandas as pd

file_path = "data/processed/orders_cleaned.csv"

orders = pd.read_csv(file_path)

print("--- Validation Results ---")
print("Rows:", len(orders))
print("Columns:", len(orders.columns))
print("Duplicate order IDs:", orders["order_id"].duplicated().sum())
print("\nMissing values:")
print(orders.isna().sum())

print("\n--- Validation Checks ---")
assert len(orders) == 99441, "Unexpected row count"
assert orders["order_id"].isna().sum() == 0, "Missing order IDs found"
assert orders["order_id"].duplicated().sum() == 0, "Duplicate IDs found"

print("All validation checks passed!")