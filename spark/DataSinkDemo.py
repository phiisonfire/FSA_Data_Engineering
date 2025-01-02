from pyspark.sql import SparkSession

from lib.logger import Log4J

if __name__ == "__main__":

    spark = SparkSession.builder \
            .appName("Data Sink Demo") \
            .master("local[3]") \
            .getOrCreate()
    
    logger = Log4J(spark)

    flightTimeParquetDF = spark.read \
                            .format("parquet") \
                            .load("dataSource/flight*.parquet")
    
    logger.info("Num partition before: " + str(flightTimeParquetDF.rdd.getNumPartitions()))
    
    '''
    flightTimeParquetDF.write \
        .format("avro") \
        .mode("overwrite") \
        .option("path", "dataSink/avro/") \
        .save()
    '''

    flightTimeParquetDF.write \
        .format("json") \
        .mode("overwrite") \
        .option("path", "dataSink/json/") \
        .partitionBy("OP_CARRIER", "ORIGIN") \
        .save()
    