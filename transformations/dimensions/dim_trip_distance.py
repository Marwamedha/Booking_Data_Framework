from pyspark.sql import SparkSession
from pyspark.sql.functions import when


def main():
    spark = SparkSession.builder.appName("dim-trip-distance").getOrCreate()
    dim_path = "/databricks/driver/data/dimensions/dim_trip_distance"

    distances = [
        (1, "0-1 mile"),
        (2, "1-3 miles"),
        (3, "3-5 miles"),
        (4, "5-10 miles"),
        (5, ">10 miles")
    ]

    df = spark.createDataFrame(distances, ["trip_distance_key", "distance_bucket"])
    df.write.mode("overwrite").parquet(dim_path)
    spark.stop()


if __name__ == "__main__":
    main()
