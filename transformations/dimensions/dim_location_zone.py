from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit


def main():
    spark = SparkSession.builder.appName("dim-location-zone").getOrCreate()
    dim_path = "/databricks/driver/data/dimensions/dim_location_zone"

    zone_data = [
        (1, "Zone A", "Zone B", "Central"),
        (2, "Zone C", "Zone D", "North"),
        (3, "Zone E", "Zone F", "East")
    ]

    df = spark.createDataFrame(zone_data, ["location_zone_key", "pickup_zone", "dropoff_zone", "region"])
    df.write.mode("overwrite").parquet(dim_path)
    spark.stop()


if __name__ == "__main__":
    main()
