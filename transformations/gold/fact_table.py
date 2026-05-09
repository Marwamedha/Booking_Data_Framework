from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def main():
    spark = SparkSession.builder.appName("fact-table").getOrCreate()
    silver_path = "/databricks/driver/data/silver/cleaned_rides"
    fact_path = "/databricks/driver/data/gold/fact_rides"

    df = spark.read.parquet(silver_path)
    fact = df.select(
        col("ride_id"),
        col("ride_timestamp"),
        col("payment_type"),
        col("pickup_zone"),
        col("dropoff_zone"),
        col("passenger_count"),
        col("trip_distance"),
        col("fare_amount"),
        col("tip_amount"),
        col("total_amount")
    )
    fact.write.mode("overwrite").parquet(fact_path)
    spark.stop()


if __name__ == "__main__":
    main()
