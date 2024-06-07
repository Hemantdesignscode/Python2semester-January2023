
import pandas as pd

NBA_data = pd.DataFrame({
    "GP" : [61, 62, 63, 60, 60, 64, 61, 63, 61, 62],
    "W" : [44, 44, 44, 39, 37, 39, 36, 36, 34, 33],
    "L" : [17, 18, 19, 21, 23, 25, 25, 27, 27, 29], 
    "WIN%" : [.721, .710, .698, .650, .617, .609, .590, .571, .557, .532], 
    "MIN" : [48.4, 48.7, 48.2, 48.4, 48.2, 48.5, 48.4, 48.7, 48.1, 48.3],
    "PTS" : [114.9, 117.7, 117.2, 113.9, 116.0, 111.9, 120.7, 114.7, 113.6, 108.0]}, index = ["1 Milwaukee Bucks", "2 Boston Celtics",
    "3 Denver Nuggets", "4 Philadelphia 76ers", "5 Memphis Grizzlies", "6 Cleveland Cavaliers", "7 Sacramento Kings", "8 New York Knicks",
    "9 Brooklyn Nets", "10 Miami Heat"])

NBA_data.index.name = "TEAM" # THIS FUNCTION OR METHOD GIVES A NAME TO ALL THE INDEX VALUES OF THE DATAFRAME

print("\n{}\n".format(NBA_data))

""" THE CODE BELOW GETS THE NUMBER OF COLUMNS AND ROWS THE DATAFRAME HAS """

rows, cols = NBA_data.shape
""" the shape function or method outputs the number of columns, rows as integers just like how we see the shape of an array """

print("1. The DataFrame includes {} rows\n".format(rows))
print("1. The DataFrame includes {} columns\n".format(cols))

""" THE CODE BELOW GETS THE DATA TYPE OF THE COLUMNS IN THE DATAFRAME USING THE DTYPE FUNCTION OR METHOD """

data_columns = NBA_data.dtypes
""" the dtypes function or method outputs the data type for each column within the DataFrame """

print("1. The data types for each of the columns are\n")
print("{}\n".format(data_columns))

""" THE CODE HERE RETRIEVES THE INFORMATION ABOUT THE BOSTON CELTICS AND THE DENVER NUGGETS """

Two_Teams = NBA_data.loc[["2 Boston Celtics", "3 Denver Nuggets"]]

print("2. The Data for the Boston Celtics and the Denver Nuggets are\n")
print("{}\n".format(Two_Teams))

""" THE CODE TO SORT THE DATAFRAME FROM HIGH TO LOW POINTS """

sorted_NBA_data = NBA_data.sort_values(by = "PTS",axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

print("3. The sorted DataFrame from the highest to the lowest points\n")
print("{}\n".format(sorted_NBA_data))

""" THE CODE TO ADD A COLUMN TO THE DATAFRAME FROM THE NBA WEBSITE OF ASSISTS """

Assists = [24.7, 26.3, 29.3, 24.9, 25.2, 24.9, 27.1, 22.4, 25.6, 23.3]

NBA_data["AST"] = Assists

print("4. The DataFrame after adding the Assists column to it\n")
print("{}\n".format(NBA_data))

""" THE CODE TO ADD A ROW TO THE DATAFRAME """

new_NBA_data = pd.DataFrame({
    "GP" : [59],
    "W" : [27],
    "L" : [32],
    "WIN%" : [.458],
    "MIN" : [48.6],
    "PTS" : [117.0],
    "AST" : [25.2]}, index = ["23 Los Angeles Lakers"])

new_NBA_data.index.name = "TEAM"

combine_data = pd.concat([NBA_data, new_NBA_data])

print("5. The DataFrame after adding the Los Angeles Lakers row to it\n")
print("{}\n".format(combine_data))

""" WRITING THE DATAFRAME TO A CSV FILE """

DataFrame_to_CSV = combine_data.to_csv("C:\\users\\heman\\Python Files 1302\\Homework\\Homework1_DataFrame_To_CSV.csv", index = True)