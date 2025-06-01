from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def load_raw_data(spark: SparkSession, filepath: str):
    df = spark.read.csv(filepath, header=True, inferSchema=True)
    return df

def validate_data(df):
    null_count = df.filter(col("machine_id").isNull() | col("timestamp").isNull()).count()
    if null_count > 0:
        raise ValueError(f"Validation failed: {null_count} rows with null machine_id or timestamp")
    return True
