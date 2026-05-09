from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, count, avg


def main():
    spark = SparkSession.builder.appName("daily-ride-metrics").getOrCreate()
    fact_path = "/databricks/driver/data/gold/fact_rides"

    df = spark.read.parquet(fact_path)
    df.withColumn("ride_date", to_date("ride_timestamp"))
    df.groupBy("ride_date").agg(
        count("ride_id").alias("total_rides"),
        avg("total_amount").alias("avg_total_amount")
    ).show()
    spark.stop()


if __name__ == "__main__":
    main()
