
This repository focuses on providing interview scenario questions that I have encountered during interviews. The questions are designed to simulate real-world scenarios and test your problem-solving and technical skills. By exploring these scenarios, you can gain insights into common interview topics and prepare yourself for similar challenges.


**Scenario 1
**Input **
Requirement already satisfied: pyspark in /usr/local/lib/python3.11/dist-packages (3.5.5)
Requirement already satisfied: py4j==0.10.9.7 in /usr/local/lib/python3.11/dist-packages (from pyspark) (0.10.9.7)
+-------+-------------------+
|food_id|          food_item|
+-------+-------------------+
|      1|        Veg Biryani|
|      2|     Veg Fried Rice|
|      3|    Kaju Fried Rice|
|      4|    Chicken Biryani|
|      5|Chicken Dum Biryani|
|      6|     Prawns Biryani|
|      7|      Fish Birayani|
+-------+-------------------+

+-------+------+
|food_id|rating|
+-------+------+
|      1|     5|
|      2|     3|
|      3|     4|
|      4|     4|
|      5|     5|
|      6|     4|
|      7|     4|
+-------+------+

Output
+-------+-------------------+------+------------+
|food_id|          food_item|rating|rating_stars|
+-------+-------------------+------+------------+
|      1|        Veg Biryani|     5|       *****|
|      2|     Veg Fried Rice|     3|         ***|
|      3|    Kaju Fried Rice|     4|        ****|
|      4|    Chicken Biryani|     4|        ****|
|      5|Chicken Dum Biryani|     5|       *****|
|      6|     Prawns Biryani|     4|        ****|
|      7|      Fish Birayani|     4|        ****|
+-------+-------------------+------+------------+
