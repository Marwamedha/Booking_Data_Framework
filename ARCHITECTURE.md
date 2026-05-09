# Architecture

## Overview

This project uses a Medallion architecture pattern:

- Bronze: raw ingestion of ride source data
- Silver: data quality, parsing, and enrichment
- Gold: business-ready analytic tables and views

## Layers

### Bronze
- Ingest raw CSV or Delta source data
- Store raw records with minimal transformation

### Silver
- Clean and validate ride events
- Build dimension tables for time, payment, location, passenger count, and trip distance

### Gold
- Build star schema fact table
- Generate analytics views for payments, daily metrics, trip patterns, and geographic zone analysis

## Deployment targets

- Databricks Workspace
- GitHub repository for version control
- Optional Event Hubs or streaming ingestion
