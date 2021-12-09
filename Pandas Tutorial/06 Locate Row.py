"""
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

#refer to the row index:
print(df.loc[0])

#use a list of indexes:
print(df.loc[[0, 1]])

# When using [], the result is a Pandas DataFrame.