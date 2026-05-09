from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, avg


def main():
    spark = SparkSession.builder.appName("payment-analysis").getOrCreate()
    fact_path = "/databricks/driver/data/gold/fact_rides"

    df = spark.read.parquet(fact_path)
    df.groupBy("payment_type").agg(
        _sum("total_amount").alias("revenue"),
        avg("fare_amount").alias("avg_fare")
    ).show()
    spark.stop()


if __name__ == "__main__":
    main()
