from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Learning').getOrCreate()

df = spark.read.csv('./vgsales.csv',header=True, inferSchema=True)

df.printSchema()
