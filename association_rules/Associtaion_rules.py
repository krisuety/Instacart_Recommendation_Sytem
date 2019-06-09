import numpy as np
import pandas as pd
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)
from pyspark.sql.functions import col, when
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
from pyspark.ml.fpm import FPGrowth


priors = spark.read.option('header', 'True').csv('../dataset/order_products__prior.csv')
products = spark.read.option('header', 'True').csv('../dataset/products.csv').drop('aisle_id', 'department_id')
df = priors.select('order_id', 'product_id')

# replace product_id with product_name
df = df.join(products, on='product_id', how='inner').drop('product_id')
df = df.groupby("order_id").agg(F.collect_list("product_name"))
df = df.withColumnRenamed("collect_list(product_name)", "items")

# use when item > 1
df = df.where(F.size(F.col("items")) > 1)

# generate associate rules
fp = FPGrowth(itemsCol="items", minSupport=0.0001, minConfidence=0.0001)
fpm = fp.fit(df)
result = fpm.associationRules


# set one item to one item (because too many items in data)
result = result_confidence.where(F.size(F.col("antecedent")) == 1)
result = result_confidence.where(F.size(F.col("consequent")) == 1)

top5_lift = result.sort(result.lift.desc()).take(5)
top5_lift_df = sqlContext.createDataFrame(top5_lift)

top5_confidence = result.sort(result.confidence.desc()).take(5)
top5_confidence_df = sqlContext.createDataFrame(top5_confidence)
