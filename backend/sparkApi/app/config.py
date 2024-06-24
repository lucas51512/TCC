import os

HDFS_HOST = os.getenv('HDFS_HOST', 'hdfs://localhost:9000')
SPARK_MASTER = os.getenv('SPARK_MASTER', 'spark://localhost:7077')
