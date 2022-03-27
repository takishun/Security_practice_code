#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import warnings
import base64
warnings.simplefilter('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('/Users/takishun/files20220327/access_log.txt',delimiter=' ',names=('ymd','time','from_ip_adress','to_ip_address','HTTP','response','TorF','basic64'))


# In[3]:


data['ymd']=data['ymd'].str.replace('[','')
data['time']=data['time'].str.replace(']','')
data['time']=pd.to_datetime(data['ymd'] + ' ' + data['time'],format='%Y-%m-%d %H:%M:%S+0900')
data['ymd']=pd.to_datetime(data['ymd'],format='%Y-%m-%d')


# In[4]:


data


# In[5]:


for i in range(0,len(data['basic64'])):
    data['basic64'][i] = base64.b64decode(data['basic64'][i]).decode()


# In[6]:


b64_decL = [base64.b64decode(data['basic64'][i]).decode().split('\n') for i in range(0,len(data['basic64']))] 


# In[ ]:


data['res']=data['HTTP']
data['url']=data['HTTP']
for i in range(0,len(data['HTTP'])):
    data['res'][i] = data['HTTP'].str.split()[i][0]
    data['url'][i] = data['HTTP'].str.split()[i][2]


# In[7]:


data


# In[15]:


class log_analytic_code:
    def __init__(self,fpass):
        import pandas as pd
        import matplotlib.pyplot as plt
        import warnings
        import base64
        warnings.simplefilter('ignore')
        get_ipython().run_line_magic('matplotlib', 'inline')
        self.fpass = pd.read_csv(fpass,delimiter=' ',names=('ymd','time','from_ip_adress','to_ip_address','HTTP','status_code','TorF','basic64'))
    
    def make_access_plot(self):
        print('daily access count')
        self.fpass['ymd'].value_counts().plot(color='orange',figsize=(15,15))
        plt.xlabel('日付')
        plt.ylabel('アクセス数')
        plt.grid()
        plt.savefig('access_count.png')
    
    def make_ip_count(self,rank_c):
        print('up address count start')
        self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False).head(rank_c).plot(kind='bar',figsize=(15,15))
        self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False).to_csv('ip.csv')
        print(self.fpass['from_ip_adress'].value_counts().sort_values(ascending=False).head(rank_c))
        plt.ylabel('アクセス数')
        plt.xlabel('ipアドレス')
        plt.savefig('ip_adress_count.png')
        
    def make_response_plot(self):
        print('status code aggrication start')
        
        self.fpass['status_code'].value_counts().sort_values(ascending=False).plot(kind='bar',figsize=(15,20))
        print(self.fpass['status_code'].value_counts().sort_values(ascending=False))
        plt.ylabel('頻度')
        plt.xlabel('ステータスコード')
        plt.savefig('status_code.png')
        
    def make_url_plot(self,rank_c):
        print('url_aggrication_start')
        self.fpass['url'].value_counts().sort_values(ascending=True).head(rank_c).plot(kind='bar',figsize=(15,20))
        print(self.fpass['url'].value_counts().sort_values(ascending=True))
        plt.ylabel('頻度')
        plt.xlabel('url')
        plt.savefig('url.png')
    
    def make_httpres_plot(self):
        print('httpres_process')
        self.fpass['res'].value_counts().sort_values(ascending=True).head().plot(kind='bar',figsize=(15,20))
        print(self.fpass['res'].value_counts().sort_values(ascending=True))
        plt.ylabel('頻度')
        plt.xlabel('res')
        plt.savefig('res.png')        
    
    def display(self):
        print(self.fpass)
    
    def mung(self):
        print('process start')
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
        print('end of data mungging')
            
        return self.fpass

if __name__ == "__main__":
    log_an = log_analytic_code('/Users/takishun/files20220327/access_log.txt') 
    log_an.mung()
    log_an.make_access_plot()
    log_an.make_ip_count(10)
    log_an.make_url_plot(10)
    log_an.make_response_plot()
    log_an.make_httpres_plot()
    print('log_process_end')
    
    


# In[182]:


a = log_analytic_code('/Users/takishun/files20220327/access_log.txt') 
a.mung()
a.make_ip_count(10)

