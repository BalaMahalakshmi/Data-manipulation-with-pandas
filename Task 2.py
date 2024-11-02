import pandas as pd
data = pd.read_csv("C:\\Users\\Mathivathanan\\Downloads\\01.Data Cleaning and Preprocessing.csv")
print(type (data))
pd.core.frame.DataFrame
data.info()
data.describe()
data=data.drop_duplicates()
print(type(data))
print(data.isnull())
print(data.isnull().sum())
print(data.notnull())
print(data.isnull().sum().sum())
data2=data.fillna(value=0)
print(data2)
data3=data.fillna(method='pad')
print(data3)
data4=data.fillna(method='bfill')
print(data4)

import numpy as np
from scipy import stats

print(data2.columns)
data2=data2.drop(['observation'], axis=1, inplace=True)
print(data2)
print(data)
print(data2.columns)
Q1=data2.quantile(0.25)
Q3=data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)
data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
print(data2.describe())



