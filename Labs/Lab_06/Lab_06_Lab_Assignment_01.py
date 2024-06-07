
import pandas as pd

Athletics = {
    "Profession": pd.Series(["BasketBall","American Football","Soccer"], name="col_one", index = ["Lebron_James","Tom_Brady","Leo_Messi"]),
    "Age": pd.Series([38, 45, 35], name="col_two", index = ["Lebron_James","Tom_Brady","Leo_Messi"]),
    "Salary": pd.Series(["45 million","15 million","41 million"], name="col_three", index = ["Lebron_James","Tom_Brady","Leo_Messi"])
}

Sports_data = pd.DataFrame(Athletics, index = ["Lebron_James","Tom_Brady","Leo_Messi"])

print("\n",Sports_data,"\n")