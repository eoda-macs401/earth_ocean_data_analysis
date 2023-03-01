#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
from matplotlib import pyplot as plt


# In[2]:


mybirthday = datetime.datetime(1983, 1, 15, 7, 15, 0, 2750)


# In[3]:


print(mybirthday)


# In[4]:


type(mybirthday)


# In[5]:


mytime = datetime.datetime.now()


# In[6]:


print(mytime)


# In[7]:


myage = mytime-mybirthday


# In[8]:


type(myage)


# In[9]:


myage.days/365


# In[10]:


get_ipython().system(' head ../data/ERSST_nearForks.csv')


# In[11]:


df = pd.read_csv('../data/ERSST_nearForks.csv', parse_dates=[0])


# In[12]:


df.info()


# In[13]:


df.plot()


# Let's pretend like we're startig from scratch with an array of values:

# In[14]:


temps = df.iloc[:,1].tolist()


# In[15]:


type(temps)


# In[16]:


dates = pd.date_range('1854-01', periods=df.shape[0], freq='MS')


# In[17]:


dates


# In[18]:


print(df.iloc[-1][0])


# In[19]:


sst = pd.Series(temps, index=dates)


# In[20]:


sst.loc['2022-01':'2022-12']


# In[21]:


sst.plot(figsize=(18,10))


# In[22]:


sst.loc['2010':'2022'].plot(figsize=(18,5))


# In[ ]:




