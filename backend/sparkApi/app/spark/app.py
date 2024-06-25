from fastapi import FastAPI
from pyspark.sql import SparkSession
from .database import MONGO_DETAILS

app = FastAPI()

spark = SparkSession.builder \
    .appName("FastAPI PySpark MongoDB") \
    .master("spark://spark-master:7077") \
    .config("spark.mongodb.input.uri", MONGO_DETAILS) \
    .config("spark.mongodb.output.uri", MONGO_DETAILS) \
    .getOrCreate()

@app.get("/")
async def root():
    return {"message": "Hello World"}