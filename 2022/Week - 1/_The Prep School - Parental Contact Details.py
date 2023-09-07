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


# In[5]:


df = pd.read_csv("PD 2022 Wk 1 Input - Input.csv")


# In[6]:


df.head()


# In[7]:


df1 = df


# In[8]:


df2 = df


# In[10]:


df.dtypes


# In[14]:


df1["Pupil's Name"] = df1["pupil last name"] + "," +df1["pupil first name"]


# In[15]:


df1["Pupil's Name"]


# In[16]:


df1.head()


# In[18]:


df1["Parental Contact Full Name"] = df1[["pupil last name","Parental Contact Name_1"]].apply(",".join,axis = 1)


# In[19]:


df1["Parental Contact Full Name"]


# In[21]:


df1.head(10)


# In[22]:


df1["Parental Contact Email Address"] = df1["Parental Contact Name_1"]+"."+df1["pupil last name"]+"@"+df1["Preferred Contact Employer"]+".com"


# In[23]:


df1["Parental Contact Email Address"]


# In[24]:


df1.head()


# In[26]:


df1["Date of Birth"] =pd.to_datetime(df1["Date of Birth"])


# In[27]:


df1.dtypes


# In[29]:


df1['Academic Year'] = 2015 - df1['Date of Birth'].apply(lambda x: x.year if x.month >= 9 else x.year-1)


# In[31]:


df1.head(10)


# In[33]:


df2= df[["Academic Year","Pupil's Name","Parental Contact Full Name","Parental Contact Email Address"]]


# In[35]:


df2.head(10)


# In[40]:


df2.to_csv("2022-Week-1.csv",index = False)


# In[ ]:




