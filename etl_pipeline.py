from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.ingestion import load_raw_data, validate_data
from src.transformation import clean_and_transform
from src.feature_engineering import create_features
from pyspark.sql import SparkSession

def etl():
    spark = SparkSession.builder.appName("PredictiveMaintenanceETL").getOrCreate()

    # Load raw sensor data
    sensor_df = load_raw_data(spark, "/data/raw/sensor_data.csv")
    validate_data(sensor_df)

    # Clean and transform
    clean_df = clean_and_transform(sensor_df)

    # Feature engineering
    feature_df = create_features(clean_df)

    # Save features parquet
    feature_df.write.mode("overwrite").parquet("/data/processed/features.parquet")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 6, 1),
    "retries": 1,
}

with DAG(
    "predictive_maintenance_etl",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    run_etl = PythonOperator(task_id="run_etl", python_callable=etl)
