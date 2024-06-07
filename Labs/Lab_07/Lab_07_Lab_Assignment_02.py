
import pandas as pd
import numpy as np

data_df = pd.DataFrame({"Name": ["Asha", "Harsh", "Sourav", "Riya", "Hritik", 
            "Shivansh", "Rohan", "Akash", "Soumya", "Kartik"], 

            "Department" : ["Administration", "Marketing", "Technical", "Technical", "Marketing", 
                    "Administration", "Technical", "Marketing", "Technical", "Administration"], 

            "Employment Type" : ["Full-time Employee", "Intern", "Intern", "Part-time Employee", "Part-time Employee",
                        "Full-time Employee", "Full-time Employee", "Intern", "Intern", "Full-time Employee"],
            
            "Salary" : [120000, 50000, 70000, 70000, 55000,
                    120000, 125000, 60000, 50000, 120000],

            "Years of Experience" : [5, 1, 2, 3, 4,
                                     7, 6, 2, 1, 6],})

""" GROUP DATAFRAME BASED ON EMPLOYMENT TYPE AND DEPARTMENT """

group = data_df.groupby(["Employment Type", "Department"])["Salary"].agg(["mean", "std", "sum", "min", "max"])
print("\n{}\n".format(group))