
import pandas as pd

file_path = "data/processed/orders_transformed.csv"

orders = pd.read_csv(file_path)

# Expected columns
expected_columns = [
    "purchase_date",
    "delivery_days",
    "estimated_delivery_days",
    "delivery_delay_days"
]

print("--- Transformed Data Validation ---")
print("Rows:", len(orders))
print("Columns:", len(orders.columns))

# Check new columns
for column in expected_columns:
    print(f"{column}: {'Present' if column in orders.columns else 'Missing'}")

# Check missing values in new columns
print("\n--- Missing Values in New Columns ---")
print(orders[expected_columns].isna().sum())

# Check delivery durations
print("\n--- Delivery Duration Checks ---")
print("Negative delivery days:", (orders["delivery_days"] < 0).sum())
print("Negative estimated days:", (orders["estimated_delivery_days"] < 0).sum())

# Check delay calculation
expected_delay = (
    orders["delivery_days"] - orders["estimated_delivery_days"]
)

difference = (
    orders["delivery_delay_days"] - expected_delay
).abs()

print("Delay calculation mismatches:", difference.gt(0.000001).sum())

# Basic assertions
assert len(orders) == 99441
assert all(column in orders.columns for column in expected_columns)
assert (orders["delivery_days"].dropna() >= 0).all()
assert (orders["estimated_delivery_days"].dropna() >= 0).all()
assert difference.dropna().le(0.000001).all()

print("\nAll validation checks passed!")