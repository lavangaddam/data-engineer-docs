# Olist E-Commerce Data Engineering Project

## 1. Executive Summary

This project explores a practical data engineering workflow using the Brazilian Olist e-commerce dataset. I built a pipeline in Python to clean, transform, validate, and load order data into SQLite and PostgreSQL. I then used SQL to analyze delivery performance and order trends and created a Power BI dashboard to visualize the results.

The project helped me understand how raw business data can be converted into structured, validated data that supports reporting and analysis.

## 2. Introduction

E-commerce platforms generate large amounts of data through orders, customers, payments, products, and deliveries. Making this data useful requires more than simply loading CSV files into a database.

For this project, I focused on the order dataset from Olist. My goal was to build a small but practical data pipeline that covers the main steps of data preparation, database loading, and business analysis.

## 3. Project Objectives

- Inspect and understand the raw order dataset.
- Clean inconsistent values and handle missing data.
- Transform timestamps into useful delivery metrics.
- Validate the processed dataset.
- Load the transformed data into SQLite and PostgreSQL.
- Write SQL queries to examine order and delivery performance.
- Build a Power BI dashboard to present key findings.
- Document the workflow in a reproducible project structure.

## 4. Dataset and Business Context

The project uses the Olist Brazilian e-commerce dataset. The order records include order identifiers, customer identifiers, order status, purchase timestamps, approval timestamps, carrier handover timestamps, delivery timestamps, and estimated delivery dates.

These fields make it possible to examine order volume and compare actual delivery performance with estimated delivery dates.

The analysis in this report focuses on the order dataset rather than the complete Olist data model.

## 5. Project Architecture

The workflow follows this sequence:

Raw CSV Data  
↓  
Python Data Inspection  
↓  
Data Cleaning  
↓  
Data Transformation  
↓  
Data Validation  
↓  
SQLite / PostgreSQL  
↓  
SQL Analysis  
↓  
Power BI Dashboard

The Python scripts handle data preparation and loading. SQL is used for analysis, while Power BI provides a visual view of the results.

## 6. Data Preparation

### 6.1 Data Inspection

I started by inspecting the raw data to understand its structure, column names, data types, and missing values. This helped identify the timestamp fields and the order identifiers that needed particular attention.

### 6.2 Data Cleaning

The cleaning script performs the following tasks:

- Removes unnecessary whitespace from selected text fields.
- Standardizes order status values to lowercase.
- Converts timestamp fields into datetime values.
- Checks for missing order IDs.
- Checks for duplicate order IDs.
- Reports missing values without automatically filling missing timestamps.

The cleaned dataset contains **99,441 rows and 8 columns**.

Missing delivery-related timestamps are preserved because a missing delivery date does not necessarily mean that the record is invalid. It may indicate an order that had not reached that stage of the delivery process.

### 6.3 Data Transformation

The transformation script creates additional fields from the cleaned order data:

- `purchase_date`: the date of purchase.
- `delivery_days`: the time between purchase and actual delivery.
- `estimated_delivery_days`: the estimated delivery duration.
- `delivery_delay_days`: the difference between actual and estimated delivery durations.

These fields make it easier to analyze delivery performance without repeating the calculations in every query.

The transformed dataset contains **99,441 rows and 12 columns**.

## 7. Data Validation

Validation was an important part of the workflow. I checked the processed data to catch problems before loading it into the databases.

The checks included:

- Duplicate order identifiers.
- Missing delivery-related fields.
- Negative delivery durations.
- Differences between calculated and stored delivery metrics.
- Record counts before and after processing.

The validation checks found no duplicate order IDs in the cleaning check, no negative delivery durations, and no mismatches in the delivery calculations.

There were **2,965 records with missing delivery fields**. These records were retained rather than removed automatically.

## 8. Database Implementation

### 8.1 SQLite

SQLite was used as a lightweight database for local testing and analysis.

The transformed CSV data was loaded into an `orders` table in:

`data/processed/olist.db`

The loaded table contains **99,441 rows**.

### 8.2 PostgreSQL

I also loaded the transformed dataset into PostgreSQL using SQLAlchemy and pandas.

The loader reads the database connection string from the `DATABASE_URL` environment variable. This avoids hardcoding database credentials in the Python script.

The PostgreSQL loading process was tested successfully in my local environment.

For security, database credentials should be configured locally and should never be committed to the repository.

## 9. SQL Analysis

I used SQL queries to examine order volume and delivery performance.

The analysis produced the following results:

| Metric | Result |
|---|---:|
| Total orders | 99,441 |
| Delivered orders | 96,478 |
| Highest monthly order volume | 7,544 |
| Month with highest order volume | November 2017 |
| Average actual delivery duration | 12.56 days |
| Average estimated delivery duration | 23.74 days |
| Average delivery delay | -11.18 days |
| Late deliveries | 7,826 |
| On-time or early deliveries | 88,644 |

A negative average delivery delay indicates that actual delivery was, on average, earlier than the estimated delivery date.

These figures reflect the SQL analysis and its definitions. In particular, delivery metrics depend on which orders have the required timestamps and how late deliveries are classified.

## 10. Power BI Dashboard

I created a Power BI dashboard named `OlistOrder_Analysis`.

The dashboard includes views of:

- Customer distribution by state.
- Order status.
- Order trends over time.
- Delivery performance.
- Delivery delays.
- Order volume by weekday.

The dashboard provides a visual way to explore the order data and complement the SQL analysis.

The Power BI file is stored in the `powerbi/` directory.

## 11. Project Structure

```text
data-engineering-project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── analysis/
├── src/
│   └── scripts/
│       ├── python/
│       │   ├── clean_orders.py
│       │   ├── inspect_data.py
│       │   ├── load_customers.py
│       │   ├── load_to_postgres.py
│       │   ├── load_to_sqlite.py
│       │   ├── transform_orders.py
│       │   ├── validate_orders.py
│       │   └── validate_transformed.py
│       └── sql/
│           └── analysis.sql
├── pipelines/
├── powerbi/
│   └── OlistOrder_Analysis.pbix
├── requirements.txt
├── README.md
└── REPORT.md
```

The raw and generated data files may be excluded from Git using `.gitignore`. The directory structure shown above describes the local project organization.

## 12. Challenges and Lessons Learned

One of the main lessons from this project was the importance of handling missing timestamps carefully. Removing every row with missing delivery information would have discarded potentially useful order records.

I also learned to separate cleaning, transformation, validation, and loading into individual scripts. This made the workflow easier to test and maintain.

Another practical lesson was to use environment variables for database connection settings rather than embedding credentials directly in the code.

Finally, I experienced how important it is to verify the results at each stage instead of assuming that a successful script execution guarantees correct data.

## 13. Limitations and Future Improvements

The current project focuses mainly on order data. It does not yet combine all customer, product, payment, seller, and review datasets into a single analytical model.

Possible improvements include:

- Automating the workflow using Apache Airflow.
- Adding automated data-quality tests.
- Improving logging and error handling.
- Building a more complete relational data model.
- Extending the analysis to customer and product performance.
- Deploying the pipeline to a cloud environment.
- Adding automated documentation and monitoring.

## 14. Tools and Technologies

| Technology | Purpose |
|---|---|
| Python | Data preparation and loading |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| SQL | Business analysis |
| SQLite | Local database |
| PostgreSQL | Relational database |
| SQLAlchemy | Database connectivity |
| Power BI | Dashboard and visualization |
| Git | Version control |
| GitHub | Project hosting and documentation |
| VS Code | Development environment |

## 15. Conclusion

This project gave me practical experience building a data workflow from raw CSV files through to database loading and business analysis.

By separating cleaning, transformation, validation, and loading, I created a workflow that is easier to understand and maintain. The SQL analysis and Power BI dashboard then helped turn the processed data into useful views of order volume and delivery performance.

It was a valuable hands-on project for strengthening my Python, SQL, database, and data engineering skills.

## 16. References

- Olist Brazilian E-Commerce Public Dataset, available on Kaggle:  
  https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Pandas documentation:  
  https://pandas.pydata.org/docs/
- SQLAlchemy documentation:  
  https://docs.sqlalchemy.org/
- PostgreSQL documentation:  
  https://www.postgresql.org/docs/
- Microsoft Power BI documentation:  
  https://learn.microsoft.com/power-bi/
