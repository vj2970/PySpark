from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[2]") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()
print(spark)