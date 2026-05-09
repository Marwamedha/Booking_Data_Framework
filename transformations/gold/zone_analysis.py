from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg


def main():
    spark = SparkSession.builder.appName("zone-analysis").getOrCreate()
    fact_path = "/databricks/driver/data/gold/fact_rides"

    df = spark.read.parquet(fact_path)
    df.groupBy("pickup_zone").agg(
        count("ride_id").alias("rides"),
        avg("total_amount").alias("avg_revenue")
    ).show()
    spark.stop()


if __name__ == "__main__":
    main()
