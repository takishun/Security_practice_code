#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from log_an_ver2 import *
import japanize_matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')

# if __name__ == "__main__":
#     start = t.time()
#     log_an = log_analytic_code('/Users/takishun/files/log20240630/log.txt','GeoLite2-City.mmdb') 
#     try: 
#         df = log_an.mung()
#         log_an.make_access_plot()
#         log_an.make_ip_count(10)
#         log_an.make_url_plot(10)
#         log_an.make_response_plot()
#         log_an.make_httpres_plot()
#         log_an.ip_country()
#         log_an.save_csv()
#     except:
#         print('except')
#     print('log_process_end: {}[sec]'.format(t.time()-start))


# In[5]:


log_an = log_analytic_code('/Users/takishun/files/log20240803/log.txt','GeoLite2-City.mmdb')
df = log_an.mung()


# # ハニーレポート7月号

# 今月のハニーポットのアクセスログの集計をレポートします。

# # デイリーアクセス

# 今月のデイリーアクセス数。

# In[6]:


log_an.make_access_plot()


# # IPアドレス別アクセス数トップ１０

# In[7]:


log_an.make_ip_count(10)


# # ステータスコード別アクセス数

# In[8]:


log_an.make_response_plot()


# # HTTPレスポンス別アクセス数

# In[9]:


log_an.make_httpres_plot()


# # 国別アクセス数

# In[10]:


log_an.ip_country()


# In[11]:


get_ipython().system('jupyter nbconvert --to html data_process.ipynb --no-input')


# In[ ]:




