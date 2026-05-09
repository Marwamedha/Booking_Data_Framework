# Sample exploration workflow for Databricks

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sample-exploration").getOrCreate()

bronze_path = "/databricks/driver/data/bronze/uber_rides"
silver_path = "/databricks/driver/data/silver/cleaned_rides"

sample_df = spark.read.parquet(silver_path).limit(100)
sample_df.printSchema()
sample_df.show(20, truncate=False)

spark.stop()
