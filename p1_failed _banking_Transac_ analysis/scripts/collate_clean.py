


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, regexp_replace, trim
from pyspark.sql.types import DoubleType

# Initialize Spark session
spark = SparkSession.builder.appName("TransactionDataCleaning").getOrCreate()

# Set the input and output paths in the GCS bucket
BUCKET_NAME = "my-bucket-rashid"
RAW_FOLDER = "gs://" + BUCKET_NAME + "/data/**"
CLEANED_FOLDER = "gs://" + BUCKET_NAME + "/cleaned/"

# Read all CSV files from the raw folder
df = spark.read.option("header", "true").option("inferSchema", "true").csv(RAW_FOLDER)

# Data Cleaning Steps

# 1. Remove duplicate rows
df = df.dropDuplicates()

# 2. Convert 'Date' column to proper date format
df = df.withColumn("Date", to_date(col("Date"), "yyyy-MM-dd"))

# 3. Remove rows with invalid or missing dates
df = df.na.drop(subset=["Date"])

# 4. Convert 'Amount' column to DoubleType and fill nulls with 0
df = df.withColumn("Amount", col("Amount").cast(DoubleType()))
df = df.na.fill({"Amount": 0})

# 5. Clean 'Branch_ID' column by removing spaces and trimming text
df = df.withColumn("Branch_ID", trim(regexp_replace(col("Branch_ID"), "\s+", "")))

# Show a sample of cleaned data
df.show(5)

# Write the cleaned data back to the cleaned folder
df.write.mode("overwrite").option("header", "true").csv(CLEANED_FOLDER)

print("Data cleaning completed.")

# Stop the Spark session
spark.stop()
