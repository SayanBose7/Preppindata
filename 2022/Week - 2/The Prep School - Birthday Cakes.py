#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import os


# In[4]:


os.listdir()


# In[19]:


df = pd.read_csv("PD 2022 Wk 1 Input - Input.csv")


# In[20]:


df.head()


# # Delete Redundant Columns

# In[21]:


df.drop(["Parental Contact Name_1","Parental Contact Name_2","Preferred Contact Employer","Parental Contact"],axis = 1, inplace = True)


# # Concat Columns

# In[22]:


df.head()


# In[23]:


df["Pupil Name"] =  df["pupil first name"] +" " + df["pupil last name"]


# In[24]:


df.head()


# # Work with Birthday

# In[27]:


df.dtypes


# In[28]:


df["Date of Birth"] = pd.to_datetime(df["Date of Birth"])


# In[29]:


df.dtypes


# In[32]:


df["This Year's Birthday"] = df["Date of Birth"].map(lambda x : x.replace(year=2021 if x.month >= 9 else 2022))


# In[33]:


df.head()


# In[34]:


df["Cake Needed On"] = df["This Year's Birthday"].dt.day_name()


# In[35]:


df.head(10)


# ### if the birthday falls on a Saturday or Sunday, we need to change the weekday to Friday

# In[37]:


df["Cake Needed On"] = df["Cake Needed On"].replace("Sunday" , "Friday")
df["Cake Needed On"] = df["Cake Needed On"].replace("Saturday" , "Friday")


# In[40]:


df.head(10)


# In[41]:


df["Month"] = df["This Year's Birthday"].dt.month_name()


# In[42]:


df.head(10)


# ### Count how many birthdays there are on each weekday in each month

# In[43]:


df['BDs per Weekday and Month'] = 1
df['BDs per Weekday and Month'] = df.groupby(['Month','Cake Needed On'])['BDs per Weekday and Month'].transform(np.sum)


# In[49]:


df_new = df[['Pupil Name','Date of Birth',"This Year's Birthday","Month","Cake Needed On",'BDs per Weekday and Month']]


# In[50]:


df_new.head(10)


# In[ ]:




