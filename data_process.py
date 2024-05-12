#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('log_df.csv')


# In[10]:


df[df['from_ip_address']=='61.244.206.142'].country


# In[8]:


df.basic64[0]


# In[ ]:




