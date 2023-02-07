# basic
import numpy as np
import pandas as pd
#import os

# get data
import pandas_datareader as pdr

# visual
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

#time
import datetime as datetime

################################################

def moving_average(df, days=5):
    #de = df.rolling(days).mean().apply(lambda x : (x-np.min(x))/(np.max(x)-np.min(x))).round(2)
    de = df.rolling(days).mean().round(2)
    return de

def normalization(df):
    de = df.rolling(5).mean().apply(lambda x : (x-np.min(x))/(np.max(x)-np.min(x))).round(2)
    return de

if 1 == 1: 
    df_3231 = pd.read_csv('3231.csv')
    df_3231 = pdr.DataReader('3231.TW', 'yahoo')
    startTime = '2012-1-01'
    endTime = '2022-10-30'
    df_3231 = pdr.DataReader('3231.TW', 'yahoo', startTime, endTime)
    df_3231.to_csv('3231.csv')
    print ("Create 3231.csv")
df_3231 = pd.read_csv('3231.csv')
print ("Open 3231.csv")
    
df_3231_20 = moving_average(df_3231, 20)
df_3231_60 = moving_average(df_3231, 60)

fig = plt.figure()
#df_3231['Adj Close'].plot(label="緯創")
df_3231_20['Adj Close'].plot(label="緯創_20")
df_3231_60['Adj Close'].plot(label="緯創_60")
df_3231_diff_60_20 = df_3231_60 - df_3231_20
df_3231_diff_60_20_n = normalization( df_3231_diff_60_20 )
#df_3231_diff_60_20_n['Adj Close'].plot(label="緯創_60-20")

df_3231_00_close_n = normalization( df_3231 )
df_3231['Adj Close'].plot(label="緯創")
plt.legend()