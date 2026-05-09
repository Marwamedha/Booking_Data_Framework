# Setup

## Requirements

- Python 3.10+
- Git
- Databricks CLI (optional)
- PySpark or Databricks runtime

## Install dependencies

```bash
pip install pyspark
```

## Running the pipeline

```bash
cd /workspaces/Booking_Data_Framework
python transformations/ingest.py
python transformations/silver/rides_cleaned.py
python transformations/gold/fact_table.py
```

## GitHub push

```bash
git add .
git commit -m "Add project files"
git push origin main
```
