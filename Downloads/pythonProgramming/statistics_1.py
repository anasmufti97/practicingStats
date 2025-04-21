
import pandas as pd 
import numpy as np

df = pd.read_csv("/Users/apple/Downloads/pythonProgramming/HeightWeight.csv")
print(df["Height(Inches)"])
print(df["Height(Inches)"].describe())
# print(df["Monthly Income"].quantile(.5))








