
import pandas as pd 

technologies = {
    "Courses" : ["Spark", "PySpark", "Python", "Pandas"],
    "Fee" : [20000, 25000, 22000, 30000],
    "Duration" : ["30days", "40days", "35days", "50days"],
}
index_labels = ["r1", "r2", "r3", "r4"]

df1 = pd.DataFrame(technologies, index = index_labels)

technologies2 = {
    "Courses" : ["Spark", "Java", "Python", "Go"],
    "Discount" : [2000, 2300, 1200, 2000], 
}
index_labels2 = ["r1", "r6", "r3", "r5"]

df2 = pd.DataFrame(technologies2, index = index_labels2)

""" MERGING THE DATAFRAME IN THREE WAYS WITH KEY = "COURSE" """

""" FIRST WAY TO MERGE DATAFRAME USING "INNER" """

first_data = pd.merge(left = df1, right = df2, how = "inner", on = ["Courses"])
print("\n{}\n".format(first_data))

""" SECOND WAY TO MERGE DATAFRAME USING "OUTER" """

second_data = pd.merge(left = df1, right = df2, how = "outer", on = ["Courses"])
print("\n{}\n".format(second_data))

""" THIRD WAY TO MERGE DATAFRAME USING "LEFT" """

third_data = pd.merge(left = df1, right = df2, how = "left", on = ["Courses"])
print("\n{}\n".format(third_data))

""" FOURTH WAY TO MERGE DATAFRAME USING "RIGHT" """

fourth_data = pd.merge(left = df1, right = df2, how = "right", on = ["Courses"])
print("\n{}\n".format(fourth_data))