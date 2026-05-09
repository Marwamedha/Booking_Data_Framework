from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("dim-passenger-count").getOrCreate()
    dim_path = "/databricks/driver/data/dimensions/dim_passenger_count"

    passenger_buckets = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    df = spark.createDataFrame(passenger_buckets, ["passenger_count_key", "passenger_count"])
    df.write.mode("overwrite").parquet(dim_path)
    spark.stop()


if __name__ == "__main__":
    main()
