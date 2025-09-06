import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df=pd.read_csv("stock-data-analysis/stockdata.csv")
#Getting all the columns
print(df.columns)
#Reading first 5 rows and columns 
print(df.head())
#Convert Date to datetime & set as index.
df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
print(df.index)
#Checking if there is any null value
print(df.isnull().sum())#No null values - output-0
#Shape- give us the number of rows and columns present there
print(df.shape)
#Describe the mathmatical functions of dataset like- mean,min,std etc
print(df.describe())
print(df.info())

#Closing Price Last 10.
plt.plot(df[' Close/Last'].tail(10),label='Closing Price')
plt.title("Closing Price Over 10 Years")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
#Volume over time
plt.plot(df[' Volume'].tail(10),label='Volume')
plt.title("Volume over time ")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()
#Highest & lowest closing price.
Highest=df[' Close/Last'].max()
Lowest=df[' Close/Last'].min()
print("Highest: ",Highest )
print("Lowest: ",Lowest)
#Daily returns
for col in [' Close/Last', ' Open', ' High', ' Low']:
    df[col] = df[col].str.replace('$', '', regex=False)
    df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = df[col].astype(float)

df['Daily Return'] = df[' Close/Last'].pct_change()
#Daily return histogram
sns.histplot(df['Daily Return'].dropna())
plt.show()
#Mean and std
x=df['Daily Return'].mean()
y=df['Daily Return'].std()
print("Mean: ",x)
print("Standard dervation: ",y)
#cumulative returns to show growth of $1 invested over selected period
df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()
print(df['Cumulative Return'])
#Average of last 10 closing and last 30 closing
df['MovingAverage10'] = df[' Close/Last'].rolling(10).mean()
df['MovingAverage30'] = df[' Close/Last'].rolling(30).mean()

df[[' Close/Last','MovingAverage10','MovingAverage30']].tail(60).plot(figsize=(8,4), title="Closing Price with Moving Averages")
plt.show()

sns.heatmap(df[[' Close/Last',' Open',' High',' Low',' Volume']].corr(), annot=True)
plt.show()

