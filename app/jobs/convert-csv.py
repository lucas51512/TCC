from pyspark.sql import SparkSession

from pyspark.sql import types as T
from pyspark.sql import Window
from datetime import datetime


def create_spark_session():
    spark = SparkSession.builder.getOrCreate()
    return spark

# def convert_xlsx_csv(spark, input, output):
#     ...