#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import matplotlib.pyplot as plt
import warnings
import base64
warnings.simplefilter('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[85]:


data = pd.read_csv('/Users/takishun/files20220320/access_log.txt',delimiter=' ',names=('ymd','time','from_ip_adress','to_ip_address','HTTP','response','TorF','basic64'))


# In[86]:


data['ymd']=data['ymd'].str.replace('[','')
data['time']=data['time'].str.replace(']','')
data['time']=pd.to_datetime(data['ymd'] + ' ' + data['time'],format='%Y-%m-%d %H:%M:%S+0900')
data['ymd']=pd.to_datetime(data['ymd'],format='%Y-%m-%d')


# In[87]:


data


# In[88]:


for i in range(0,len(data['basic64'])):
    data['basic64'][i] = base64.b64decode(data['basic64'][i]).decode()


# In[73]:


b64_decL = [base64.b64decode(data['basic64'][i]).decode().split('\n') for i in range(0,len(data['basic64']))] 


# In[177]:


data['res']=data['HTTP']
data['url']=data['HTTP']
for i in range(0,len(data['HTTP'])):
    data['res'][i] = data['HTTP'].str.split()[i][0]
    data['url'][i] = data['HTTP'].str.split()[i][2]


# In[178]:


data


# In[164]:


data['res'][0]


# In[140]:


data['from_ip_adress'].value_counts().sort_values(ascending=False).head(10).plot(kind='bar')


# In[106]:


data['ymd'].value_counts().plot(color='orange')


# In[ ]:





# In[181]:


class log_analytic_code:
    def __init__(self,fpass):
        import pandas as pd
        import matplotlib.pyplot as plt
        import warnings
        import base64
        warnings.simplefilter('ignore')
        get_ipython().run_line_magic('matplotlib', 'inline')
        self.fpass = pd.read_csv(fpass,delimiter=' ',names=('ymd','time','from_ip_adress','to_ip_address','HTTP','response','TorF','basic64'))
    
    def make_access_plot(self):
        self.fpass['ymd'].value_counts().plot(color='orange')
        plt.xlabel('日付')
        plt.ylabel('アクセス数')
        plt.grid()
        plt.savefig('access_count.png')
    
    def make_ip_count(self,rank_c):
        self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False).head(rank_c).plot(kind='bar')
        self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False).to_csv('ip.csv')
        print(self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False).head(rank_c))
        plt.ylabel('アクセス数')
        plt.xlabel('ipアドレス')
        plt.savefig('ip_adress_count.png')
        
    def make_response_plot(self):
        self.fpass['response'].value_counts().sort_values(ascending=False).plot(kind='bar')
        print(self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False))
        plt.ylabel('頻度')
        plt.xlabel('レスポンス')
        plt.savefig('response.png')
        
    def make_url_plot(self):
        pass
    
    def make_http_plot(self):
        pass
    
    def display(self):
        print(self.fpass)
    
    def mung(self):
        self.fpass['ymd']=self.fpass['ymd'].str.replace('[','')
        self.fpass['time']=self.fpass['time'].str.replace(']','')
        self.fpass['time']=pd.to_datetime(self.fpass['ymd'] + ' ' + self.fpass['time'],format='%Y-%m-%d %H:%M:%S+0900')
        self.fpass['ymd']=pd.to_datetime(self.fpass['ymd'],format='%Y-%m-%d')
        for i in range(0,len(data['basic64'])):
            self.fpass['basic64'][i] = base64.b64decode(self.fpass['basic64'][i]).decode()
            
        self.fpass['res']=self.fpass['HTTP']
        self.fpass['url']=self.fpass['HTTP']
        for i in range(0,len(data['HTTP'])):
            self.fpass['res'][i] = self.fpass['HTTP'].str.split()[i][0]
            self.fpass['url'][i] = self.fpass['HTTP'].str.split()[i][2]
            
        return self.fpass

if __name__ == "__main__":
    pass


# In[182]:


a = log_analytic_code('/Users/takishun/files20220320/access_log.txt') 
a.mung()
a.make_ip_count(10)


# In[183]:


a.display()


# In[ ]:




