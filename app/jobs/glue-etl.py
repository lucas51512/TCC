from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    year, 
    month, 
    dayofmonth, 
    hour, 
    weekofyear, 
    dayofweek, 
    udf, 
    col,
    row_number, 
    monotonically_increasing_id
)

from pyspark.sql import types as T
from pyspark.sql import Window
from datetime import datetime


def create_spark_session():
    spark = SparkSession.builder.getOrCreate()
    return spark


"""
    This procedure processes song files whose filepath has been provided as an arugment.
    It extracts the song information in order to store it into songs table and then stores it in delta format.
    It also extracts the artist information in order to store it into artists table and then stores it in delta format.

    INPUTS:
    * spark the spark connection variable
    * input_data the s3 bucket path to the song data
    * output_data the s3 bucket path to store songs and artists table
"""


"""
    This procedure processes log files whose filepath has been provided as an arugment.
    It extracts the song start time information, tansforms it and then store it into the time table in delta format.
    Then it extracts the users information in order to store it into the users table in delta format.
    Finally it extrats informations from songs table and original log file to store it into the songplays table in delta format.

    INPUTS:
    * spark the spark connection variable
    * input_data the s3 bucket path to the log data
    * output_data the s3 bucket path to store users, time and song_plays table
"""    

def main():
    spark = create_spark_session()
    input_data = "s3://tcc-landing-zone-s3-654654318164/"
    output_data = "s3://tcc-domain-bronze-s3-654654318164/"
    

if __name__ == "__main__":
    main()