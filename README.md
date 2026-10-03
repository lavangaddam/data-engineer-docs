# Olist E-Commerce Data Engineering Project

An end-to-end data engineering project using the Olist Brazilian e-commerce dataset. Built with Python, SQL, SQLite, PostgreSQL, and Power BI.

## Overview

I built a data pipeline to clean, transform, validate, and load order data into databases. I then used SQL to analyze delivery performance and order trends and created a Power BI dashboard to visualize the results.

## Workflow

Raw CSV Data → Python Cleaning → Transformation → Validation → SQLite / PostgreSQL → SQL Analysis → Power BI

## Key Results

- Processed 99,441 orders.
- Created a transformed dataset with 12 columns.
- Identified 2,965 records with missing delivery fields.
- Calculated an average delivery duration of 12.56 days.
- Calculated an average estimated delivery duration of 23.74 days.
- Identified 7,826 late deliveries using the project's calculation.

## Technologies

Python, Pandas, NumPy, SQL, SQLite, PostgreSQL, SQLAlchemy, Power BI, Git, and GitHub.

## Project Report

[Read the full project report](REPORT.md)

## Dashboard

The Power BI dashboard file is available at `powerbi/OlistOrder_Analysis.pbix`.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/lavangaddam/data-engineer-docs.git
cd data-engineer-docs
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the main processing workflow:

```bash
python src/scripts/python/clean_orders.py
python src/scripts/python/transform_orders.py
python src/scripts/python/validate_orders.py
python src/scripts/python/validate_transformed.py
python src/scripts/python/load_to_sqlite.py
```

To load into PostgreSQL, configure `DATABASE_URL` for your local database and run:

```bash
python src/scripts/python/load_to_postgres.py
```

The raw Olist dataset must be downloaded separately and placed in `data/raw/` before running the scripts.

## Author

**Lavan Kumar Gaddam**

Data Science master's student interested in data engineering, analytics, and practical data workflows.

[GitHub Profile](https://github.com/lavangaddam)
