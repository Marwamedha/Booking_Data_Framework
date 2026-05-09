from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit


def main():
    spark = SparkSession.builder.appName("dim-payment-type").getOrCreate()
    dim_path = "/databricks/driver/data/dimensions/dim_payment_type"

    payment_types = [
        (1, "Credit Card"),
        (2, "Cash"),
        (3, "Mobile Payment"),
        (4, "Other")
    ]

    df = spark.createDataFrame(payment_types, ["payment_type_key", "payment_type"])
    df.write.mode("overwrite").parquet(dim_path)
    spark.stop()


if __name__ == "__main__":
    main()
