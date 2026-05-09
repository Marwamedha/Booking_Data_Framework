from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, dayofmonth, hour, dayofweek, quarter


def main():
    spark = SparkSession.builder.appName("dim-datetime").getOrCreate()
    silver_path = "/databricks/driver/data/silver/cleaned_rides"
    dim_path = "/databricks/driver/data/dimensions/dim_datetime"

    df = spark.read.parquet(silver_path)
    dim = df.select(col("ride_timestamp").alias("ride_timestamp"))
    dim = dim.withColumn("datetime_key", col("ride_timestamp").cast("long"))
    dim = dim.withColumn("ride_date", col("ride_timestamp").cast("date"))
    dim = dim.withColumn("ride_hour", hour(col("ride_timestamp")))
    dim = dim.withColumn("day_of_week", dayofweek(col("ride_timestamp")))
    dim = dim.withColumn("month", month(col("ride_timestamp")))
    dim = dim.withColumn("quarter", quarter(col("ride_timestamp")))
    dim = dim.withColumn("year", year(col("ride_timestamp")))
    dim.dropDuplicates(["datetime_key"]).write.mode("overwrite").parquet(dim_path)
    spark.stop()


if __name__ == "__main__":
    main()
