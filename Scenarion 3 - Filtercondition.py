!pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Colab_PySpark").getOrCreate()

data = [
    (1, "Alice", "IT", 5000, 2),
    (2, "Bob", "HR", 6000, 5),
    (3, "Alice", "IT", 5000, 2),
    (4, "David", "Finance", 7000, 7),
    (5, "Eva", "IT", 8000, 6),
    (6, "Bob", "HR", 6000, 5),
    (7, "Grace", "Finance", 9000, 10),
    (8, "suyog",None, 9000, 10)
]

# Create DataFrame
columns = ["id", "name", "department", "salary", "experience"]
df = spark.createDataFrame(data, columns);
df.show()

#For single column filtering
sincol = df.filter("department='IT'")
sincol.show()

doublecol = df.filter("department='IT' and salary > 5000")
doublecol.show()

#in

doublecol = df.filter("department in ('IT','HR')")
doublecol.show()

#like 
doublecol = df.filter("name like 'A%'")
doublecol.show()

#check is null  
doublecol = df.filter("department is NULL")
doublecol.show()

#check is not null  
doublecol = df.filter("department is not null")
doublecol.show()
