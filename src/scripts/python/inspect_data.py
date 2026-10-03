
import pandas as pd

# 1. Load the dataset
file_path = "data/raw/olist_orders_dataset.csv"
orders = pd.read_csv(file_path)

# 2. Convert timestamp columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")

# 3. Display first 5 rows
print("\n--- First 5 Rows ---")
print(orders.head())

# 4. Dataset shape
print("\n--- Dataset Shape ---")
print(orders.shape)

# 5. Column names
print("\n--- Column Names ---")
print(orders.columns.tolist())

# 6. Missing value counts
print("\n--- Missing Values ---")
print(orders.isnull().sum())

# 7. Missing value percentages
print("\n--- Missing Value Percentages ---")
missing_percent = orders.isnull().mean() * 100
print(missing_percent.round(2))

# 8. Order status distribution
print("\n--- Order Status Distribution ---")
print(orders["order_status"].value_counts())

# 9. Missing delivery dates by order status
print("\n--- Missing Delivery Dates by Status ---")
missing_by_status = (
    orders.groupby("order_status")[
        "order_delivered_customer_date"
    ].apply(lambda column: column.isnull().sum())
)
print(missing_by_status)

# 10. Delivered orders with missing delivery dates
print("\n--- Delivered Orders With Missing Delivery Dates ---")
delivered_missing = orders[
    (orders["order_status"] == "delivered")
    & (orders["order_delivered_customer_date"].isnull())
]
print(delivered_missing)

# 11. Timestamp details for those orders
print("\n--- Timestamp Details for These Orders ---")
print(
    delivered_missing[
        [
            "order_id",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ].to_string(index=False)
)

# 12. Duplicate order IDs
print("\n--- Duplicate Order IDs ---")
print(orders["order_id"].duplicated().sum())

# 13. Column data types
print("\n--- Column Data Types ---")
print(orders.dtypes)