from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when


def main():
    spark = SparkSession.builder.appName("booking-silver").getOrCreate()
    bronze_path = "/databricks/driver/data/bronze/uber_rides"
    silver_path = "/databricks/driver/data/silver/cleaned_rides"

    df = spark.read.parquet(bronze_path)
    df = df.withColumn("ride_timestamp", to_timestamp(col("pickup_datetime"), "yyyy-MM-dd HH:mm:ss"))
    df = df.withColumn("valid_fare", when(col("fare_amount").cast("double") > 0, col("fare_amount")).otherwise(None))
    df = df.filter(col("ride_timestamp").isNotNull())
    df.write.mode("overwrite").parquet(silver_path)
    spark.stop()


if __name__ == "__main__":
    main()
