# Booking Data Framework

A complete end-to-end data engineering and analytics framework for ride-hailing data built for Databricks and GitHub.

## What is included

- Medallion architecture: Bronze, Silver, Gold
- CDC-enabled dimensions with SCD Type 1 patterns
- Star schema fact model for ride analytics
- SQL dashboard configuration with key performance visualizations
- Documentation, setup instructions, and repository structure

## Files in this repository

- `transformations/`: Spark transformation pipelines
- `explorations/`: sample exploration and Event Hubs references
- `ARCHITECTURE.md`: architecture and design decisions
- `DATA_MODEL.md`: schema documentation
- `SETUP.md`: environment setup and deploy guide
- `DASHBOARD.md`: dashboard widget definitions
- `GITHUB_PUSH_GUIDE.md`: GitHub workflow and push guide

## Quick start

```bash
cd /workspaces/Booking_Data_Framework
pip install -r requirements.txt
python transformations/ingest.py
python transformations/silver/rides_cleaned.py
python transformations/gold/fact_table.py
```

## Repository URL
## 🔗 Live Dashboard

[Click Here to Open Dashboard](https://dbc-334d6636-4d39.cloud.databricks.com/dashboardsv3/01f14ba3a4f816f2a0c1c2bc9e7a54c7/published?o=165006701026677)
![Uber Booking Dashboard](https://github.com/Marwamedha/Booking_Data_Framework/blob/main/Dashboard.jpg)


