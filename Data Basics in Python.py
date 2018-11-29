# Basics of data wrangling in Python

# Import the pandas package as pd.
# The 'as pd' allows us to reference pandas functions by just writing pd.
import pandas as pd

# Use the pandas function read_csv() to read in the file.
# File paths work the same as in R (double \\ or / required)
my_data = pd.read_csv("C:\\Users\\Roland\\Documents\\git_repositories\\LearningPython\\winemag-data-130k-v2.csv")
my_data.head()

# Need to use index_col = 0 to sort of the index column:
my_data = pd.read_csv("C:\\Users\\Roland\\Documents\\git_repositories\\LearningPython\\winemag-data-130k-v2.csv",
                      index_col = 0)
my_data.head()


# I want to select the country column from my_data.
my_data["country"]

# ^ the above does not return a dataFrame. We use [[]] to return a dataFrame:
my_data[["country"]]

# I want to select the first row of observations from my dataFrame:
my_data[0:1]

# Using loc and iloc to subset dataFrames:

# loc to reference by name:
my_data.loc[0:0,["country"]] # <- why do we use 0:0 here and 0:1 below???

# iloc to reference by index:
my_data.iloc[0:1,[0]]

