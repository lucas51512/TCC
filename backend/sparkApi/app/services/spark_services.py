from pyspark.sql import SparkSession
from app.config import HDFS_HOST, SPARK_MASTER

def run_spark_job():
    spark = SparkSession.builder \
        .master(SPARK_MASTER) \
        .appName("FastAPI Spark Job") \
        .getOrCreate()

    # Leitura de dados do HDFS
    df = spark.read.csv(f"{HDFS_HOST}/../../../dados/pokemon.csv")

    # Algoritmo Spark (exemplo: contagem de linhas)
    count = df.count()

    spark.stop()
    return count
