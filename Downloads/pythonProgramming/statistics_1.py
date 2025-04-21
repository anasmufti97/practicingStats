
import pandas as pd 
import numpy as np

df = pd.read_csv("/Users/apple/Downloads/pythonProgramming/stats.csv")

print(df)
print(df.describe())
print(df["Monthly Income"].quantile(.5))





