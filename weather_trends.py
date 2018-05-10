
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


##These are the sql queries used to extract the data used for the project. 


SELECT *
FROM city_list
WHERE country like 'United States'


### Renaming the columns for joining
ALTER TABLE global_data RENAME COLUMN avg_temp to global_avg_temp;

ALTER TABLE city_data RENAME COLUMN avg_temp to city_avg_temp;


### Downloading the joined tables
SELECT global_data.year, global_data.global_avg_temp, city_avg_temp
FROM global_data INNER JOIN city_data
ON global_data.year=city_data.year
WHERE city like 'Austin';

### Saved as gcavgtemp.csv


# In[2]:


#Using pandas to import the dataset created with SQL into python
df = pd.read_csv('Documents/gcavgtemp.csv')


# In[18]:


#moving average function

def RollingMean(windowRolling, df):
    df_1 = df.rolling(window = windowRolling, center=True, on = "year").mean()
    return df_1

#size of window
rollingWindow = 10
df_movingAverage = RollingMean(rollingWindow, df)


#plotting graph

plt.plot(df_movingAverage['year'], df_movingAverage['city_avg_temp'], 'r', label='Austin')
plt.plot(df_movingAverage['year'], df_movingAverage['global_avg_temp'],'-.b',label='Global')
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Austin versus Global values ({} year moving avg)".format(rollingWindow))
plt.show()


# Steps and Observations.
# 1. Used SQL queries to extract data from database 
# 2. Used pandas to load data into python
# 3. Used pandas.rolling_mean function
# 4. Created the line chart using matplotlib
# 
# 
# The first and most obvious trend here is that Austin's average temperature is hotter than the global average, with Austin beginning around 20 degrees celsius(69 fahrenheit) and the global average beginning around 8 degrees celsius(46 degrees fahrenheit), and this difference has been consistent over time.
# 
# I played around with the size of the window in order to find a window that would show the trends in weather over time. 
# 
# The changes in Austin's temperature seem to fluctuate a bit more than the global averages, but both temperatures are consistently getting hotter.
# 
# The overall conclusion here is that according to the data, the world is getting hotter, and this trend appears to be consistent over the last few hundred years.
# 
# 
# 
# 
# 
# Sources:http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.rolling_mean.html
# 
# https://machinelearningmastery.com/moving-average-smoothing-for-time-series-forecasting-python/
# 
# 
