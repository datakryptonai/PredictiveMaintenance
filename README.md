# Predictive Maintenance Data Pipeline

This project implements an end-to-end data pipeline for predictive maintenance using Apache Spark, Python, and Tableau.

## Features

- Data ingestion, cleaning, and transformation pipelines
- Feature engineering for machine learning
- Workflow orchestration with Apache Airflow
- Interactive Tableau dashboard for visualization

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run Airflow and start the ETL pipeline:

```bash
airflow dags trigger predictive_maintenance_etl
```

3. Explore the Tableau dashboard connecting to processed data.

## Author

Debjyoti Kar — Data Architect | Data Engineer | Data Analyst  
Email: debjyoti@datakrypton.ai  
Website: [www.datakrypton.ai](https://www.datakrypton.ai)
