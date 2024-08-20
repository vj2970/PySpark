from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Learning').getOrCreate()


dataset = spark.read.csv('vgsales.csv',header=True, inferSchema=True)
dataset.show()
print(type(dataset))