#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd


# In[44]:


import os


# In[45]:


os.listdir()


# In[46]:


df1 = pd.read_csv("PD 2022 Wk 1 Input - .csv")
df2 = pd.read_csv("PD 2022 WK 3 Grades.csv")


# ## Join the Data

# In[47]:


df = pd.merge(df1,df2,how='inner',left_on='id',right_on='Student ID')


# In[48]:


df.head()


# In[49]:


df.drop(['Parental Contact Name_1', 'Parental Contact Name_2','Preferred Contact Employer', 'Parental Contact', 'id'] , axis = 1, inplace = True)


# In[50]:


df.head()


# ## Pivot/unpivot the data

# In[51]:


df = df.melt(id_vars=['Student ID','pupil first name','pupil last name','gender','Date of Birth'], var_name='Subject', value_name='Score')


# In[52]:


df.head()


# ## Average score per student based on all of their grades

# In[53]:


df["Student's Avg Score"] = df.groupby(['Student ID'])['Score'].transform('mean')


# In[54]:


df.head()


# ## Field that records whether the student passed each subject

# In[55]:


df["Passed Subject"] = np.where(df['Score']>=75,1,0)


# ## How many subjects each student passed

# In[57]:


df = df.groupby(['Student ID','gender',"Student's Avg Score"]).agg(passed_subjects=('Passed Subject','sum')).reset_index()


# In[58]:


df = df.round({"Student's Avg Score": 1})


# ## Output

# In[59]:


df.rename( columns={'passed_subjects':'Passed Subjects','gender':'Gender'}, inplace=True )
df = df[['Passed Subjects',"Student's Avg Score",'Student ID','Gender']]


# In[60]:


df.head()


# In[ ]:




