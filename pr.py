import pandas as pd

data1 = pd.read_csv('dirty_iris.csv')
data2 = pd.read_csv('dirty_iris_standarized.csv')
data3 = pd.read_csv('wine.csv')
data4 = pd.read_csv('wine_standarized.csv')
print("Original dirty iris data:", data1)
print("Standarized dirty iris data:", data2)
print("Original wine data:", data3)
print("Standarized wine data:", data4)