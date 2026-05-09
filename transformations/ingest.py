from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def main():
    spark = SparkSession.builder.appName("booking-ingest").getOrCreate()
    raw_path = "/databricks/driver/data/raw/uber_rides.csv"
    bronze_path = "/databricks/driver/data/bronze/uber_rides"

    df = spark.read.option("header", "true").csv(raw_path)
    df = df.withColumn("source_loaded_at", col("pickup_datetime"))
    df.write.mode("overwrite").parquet(bronze_path)
    spark.stop()


if __name__ == "__main__":
    main()
