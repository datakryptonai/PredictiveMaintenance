from pyspark.sql.functions import col, to_timestamp

def clean_and_transform(df):
    # Convert timestamp to Spark timestamp type
    df = df.withColumn("timestamp", to_timestamp(col("timestamp")))
    # Filter out invalid temperature readings (sensor error values)
    df = df.filter(col("temperature") > -40)
    return df
