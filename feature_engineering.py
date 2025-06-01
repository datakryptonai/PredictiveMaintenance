from pyspark.sql import Window
from pyspark.sql.functions import avg, max, col

def create_features(df):
    window_spec = Window.partitionBy("machine_id").orderBy("timestamp").rowsBetween(-3, 0)

    df = df.withColumn("temp_mean_3h", avg(col("temperature")).over(window_spec))
    df = df.withColumn("vib_max_3h", max(col("vibration")).over(window_spec))

    df = df.na.fill(0, subset=["temp_mean_3h", "vib_max_3h"])
    return df
