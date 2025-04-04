spark = SparkSession.builder.appName("Colab_PySpark").getOrCreate()

data = [
    (1, "Alice", "IT", 5000, 2),
    (2, "Bob", "HR", 6000, 5),
    (3, "Alice", "IT", 5000, 2),
    (4, "David", "Finance", 7000, 7),
    (5, "Eva", "IT", 8000, 6),
    (6, "Bob", "HR", 6000, 5),
    (7, "Grace", "Finance", 9000, 10)
]

# Create DataFrame
columns = ["id", "name", "department", "salary", "experience"]
df = spark.createDataFrame(data, columns);
df.show()

finaldata = df.dropDuplicates(["name","department"])
finaldata.show()
