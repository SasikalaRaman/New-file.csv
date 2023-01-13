#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd # pandas library
import matplotlib.pyplot as plt # data visualization 


# In[4]:


pd.read_csv("new.csv") # read the csv files from panda library


# In[5]:


df=pd.read_csv("new.csv")
print(df) # print the output


# In[6]:


df.describe() #over all describtion of the values in the data set


# In[7]:


df["TAX"].sum() # sum the values in TAX column
 


# In[8]:


df["CRIM"].sum() # sum the values in the CRIM column


# In[9]:


df["LSTAT"].sum() # sum the values in the LSTAT column


# In[10]:


df["INDUS"].sum() # sum the values in the INDUS column


# In[11]:


Rate=["TAX","CRIM","LSTAT","INDUS"] # These are the labels for pie chart


# In[ ]:




