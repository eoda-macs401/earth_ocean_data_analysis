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


# Let's resample our data to a uniform sample rate of 30 days:

# In[23]:


sst_reg = sst.resample("30D").ffill()


# In[24]:


sst.loc['2012':'2022'].plot(figsize=(18,10))
sst_reg.loc['2012':'2022'].plot()


# In[25]:


sst_reg.loc['2020':'2022']


# In[26]:


import scipy
import numpy as np


# Here we're taking the Fourier Transform of our SST

# In[27]:


freq_spec = np.fft.fft(sst_reg.values)


# In[28]:


# First lets grab the length of our record in samples
N = sst_reg.shape[0]
print(N)


# In[29]:


#period in between samples of our discretly sampled data
t = 30 #day

#not sample rate:
sr=1/t

#get the total duration of our record:
T = N*t
print(T/365)


# In[30]:


freq = np.fft.fftfreq(N,t)
freq.shape


# In[31]:


print(max(freq))


# In[32]:


print(sr/2)


# Let's plot it up:

# In[33]:


#grab positive side of the spectrum
n_oneside = N//2 

f_oneside = freq[:n_oneside]
f_spec_oneside = np.abs(freq_spec[:n_oneside])

plt.figure(figsize = (12,6))
plt.plot(f_oneside, f_spec_oneside, 'b')


# In[34]:


plt.figure(figsize = (12,6))
plt.plot(1/f_oneside/365, f_spec_oneside, 'b')
plt.xlabel('Period, years')
plt.ylabel('FFT Amplitude')
plt.grid()

plt.xlim((0, 25))


# In[35]:


from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


# In[36]:


# converting my timeseries back to ... a number
# this will be days relative to the start of my record

dt = (sst_reg.index - sst_reg.index[0]).days.to_numpy()

dt.shape


# In[37]:


X = dt.reshape(-1,1)
X.shape


# In[38]:


y = sst_reg.to_numpy()


# Now for the model fit - this is how sklearn does it - 
# We define a model!

# In[39]:


#initialize my linear model
regr = linear_model.LinearRegression()

#fit the model based on our data and then make a predicion using our model
regr.fit(X,y)
y_pred = regr.predict(X)


# In[40]:


plt.figure(figsize=(18,10))
plt.plot(sst_reg.index, y, color="black")
plt.plot(sst_reg.index, y_pred, color="blue", linewidth=3)


# In[41]:


regr.coef_


# In[42]:


regr.intercept_


# In[43]:


r2_score(y,y_pred)


# In[44]:


sst_final= pd.DataFrame({ 'sst': sst_reg})
sst_final

sst_reg.shape


# In[45]:


plt.figure()
ax1 = sst_final.plot(figsize=(15, 9), linewidth=1, fontsize=16)


# In[ ]:




