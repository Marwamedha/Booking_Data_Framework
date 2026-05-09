from pyspark.sql import SparkSession
from pyspark.sql.functions import avg


def main():
    spark = SparkSession.builder.appName("trip-analysis").getOrCreate()
    fact_path = "/databricks/driver/data/gold/fact_rides"

    df = spark.read.parquet(fact_path)
    df.groupBy("trip_distance").agg(
        avg("fare_amount").alias("avg_fare"),
        avg("tip_amount").alias("avg_tip")
    ).show()
    spark.stop()


if __name__ == "__main__":
    main()
