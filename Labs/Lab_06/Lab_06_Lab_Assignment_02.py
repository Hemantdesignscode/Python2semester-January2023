
from Lab_06_Lab_Assignment_01 import pd
from Lab_06_Lab_Assignment_01 import Athletics

""" Adding A New Row For New Player """

New_Player = {
    "Profession": pd.Series(["BasketBall"], name = "col_one", index = ["Kevin_Durant"]),
    "Age": pd.Series([34], name = "col_two", index = ["Kevin_Durant"]),
    "Salary": pd.Series(["19 million"], name = "col_three", index = ["Kevin_Durant"])
}

Sports_data = pd.DataFrame(Athletics, index = ["Lebron_James","Tom_Brady","Leo_Messi"])

Sports_data1 = pd.DataFrame(New_Player, index = ["Kevin_Durant"])

""" Using Pandas Concat Function/Method To Add New_Player To Previous DataFrame """

New_sports_data = pd.concat([Sports_data, Sports_data1])

""" Adding a New Column To The DataFrame with Player Weight """

player_weight = ["240 pounds", "225 pounds", "148 pounds", "240 pounds"]

New_sports_data["Player Weight"] = player_weight

print("\n",New_sports_data,"\n")