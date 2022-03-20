#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 


# In[23]:


import pandas as pd
import bs4
base = 'https://www.tepco.co.jp/forecast/html/images/juyo-'
syear = 2019
eyear = 2021
ftype = '.csv'


# In[24]:


ts_data = pd.DataFrame()


# In[ ]:





# In[25]:


for year in range(syear,eyear+1):
    data = pd.read_csv('https://www.tepco.co.jp/forecast/html/images/juyo-'+ str(year) + ftype,encoding='cp932')
    


# In[26]:


ts_data


# In[ ]:




