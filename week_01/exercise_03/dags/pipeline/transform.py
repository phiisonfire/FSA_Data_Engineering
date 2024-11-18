from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import current_timestamp

from extract import fetch_all_book_data_with_ids

def transform_book_data(transformation_output_path):

    spark = SparkSession.builder \
            .appName("BookDataTransformer") \
            .getOrCreate()

    books = fetch_all_book_data_with_ids()

    # Convert to RDD and then to DataFrame
    books_rdd = spark.sparkContext.parallelize(books).map(lambda x: Row(**x))
    books_df = spark.createDataFrame(books_rdd)

    # Add ingested timestamp
    books_df = books_df.withColumn("ingested_at", current_timestamp())

    # Print schema and sample data for debugging
    books_df.printSchema()
    books_df.show()

    books_df.coalesce(1).write.mode("overwrite").csv(transformation_output_path)

    spark.stop()
    return books_df

if __name__ == "__main__":
    books_df = transform_book_data("data/test.csv")
    print(books_df)