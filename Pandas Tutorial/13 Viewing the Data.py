"""
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
"""
import pandas as pd

df = pd.read_csv("Pandas Tutorial/data.csv")

print(df.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head())

"""
There is also a tail() method for viewing the last rows of the DataFrame.
The tail() method returns the headers and a specified number of rows, starting from the bottom.
"""
print(df.tail()) 