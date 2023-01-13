import pandas as pd # pandas library
import matplotlib.pyplot as plt # data visualization 

pd.read_csv("new.csv") # read the csv files from panda library

df=pd.read_csv("new.csv")
print(df) # print the output

df.describe() #over all describtion of the values in the data set


df["TAX"].sum() # sum the values in TAX column
 
df["CRIM"].sum() # sum the values in the CRIM column

df["LSTAT"].sum() # sum the values in the LSTAT column

df["INDUS"].sum() # sum the values in the INDUS column

Rate=["TAX","CRIM","LSTAT","INDUS"] # These are the labels for pie chart



