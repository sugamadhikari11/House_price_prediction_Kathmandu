#importing Libraries;
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('FinalDataSet.csv')

#viewing dataset
dataset.head()

#describe the dataset
dataset.describe()

#checking for null values or zero values
dataset.isnull().sum()
sns.heatmap(dataset.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#cheaking for zero values
(dataset == 0).sum()
sns.heatmap(dataset == 0,yticklabels=False,cbar=False,cmap='viridis')

#checking for duplicate values
dataset.duplicated().sum() 

#removing duplicate values
dataset.drop_duplicates(inplace=True)

#filling Null by mean value
# Custom function to fill null and zero values
def fill_null_zero(data, column, value):
    data[column] = data[column].fillna(value).replace(0, value)

# Fill null and zero values with specified values
fill_null_zero(dataset, 'Bathroom', 3)
fill_null_zero(dataset, 'Parking', 2)
fill_null_zero(dataset, 'Build Year(In B.S.)', 2075)
fill_null_zero(dataset, 'Road Distance(Feet)', 14)

#checking for null values or zero values
sns.heatmap(dataset.isnull(),yticklabels=False,cbar=False,cmap='viridis')
sns.heatmap(dataset == 0,yticklabels=False,cbar=False,cmap='viridis')

#viewing corellation
corr = dataset.corr()
