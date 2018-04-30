
# coding: utf-8

# In[1]:

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:

#importing the first csv file 
city_list = pd.read_csv("Documents/city-list.csv")


# In[3]:

#removing nan values
city_list = city_list.dropna()
city_list


# In[4]:

#importing global data
global_data = pd.read_csv("Documents/global-data.csv")
global_data


# In[5]:

#creating a new database 
db = [city_list, global_data]


# In[6]:

new_db = pd.concat(db)
new_db


# In[7]:

#extracting austin,tx data from indexes 5147-5340
pd.set_option('display.max_rows', 72000)
austin_data1 = new_db.loc[5147 : 5340], new_db.columns.get_indexer(['city'])
austin_data1


# In[9]:

#calculating moving average for Austin
austin_data = np.array(austin_data1)
austin_data



