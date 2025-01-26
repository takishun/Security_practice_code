#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import warnings
import base64
import geoip2.database
import time as t
warnings.simplefilter('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')
img_dir = 'image/'
result_dir = 'result/'

class log_analytic_code:
    def __init__(self,fpass,ip_dict):
        import pandas as pd
        import matplotlib.pyplot as plt
        import warnings
        import base64
        warnings.simplefilter('ignore')
        get_ipython().run_line_magic('matplotlib', 'inline')
        self.fpass = pd.read_csv(fpass,delimiter=' ',names=('ymd','time','from_ip_address','to_ip_address','HTTP','status_code','TorF','basic64'))
        self.ip_dict = geoip2.database.Reader(ip_dict)
    
    def make_access_plot(self):
        print('日付　　アクセス数')
        print(self.fpass['ymd'].value_counts().sort_index())
        self.fpass['ymd'].value_counts().sort_index().to_csv(result_dir + 'access_count.csv')
        plt.clf()
        self.fpass['ymd'].value_counts().sort_index().plot(color='orange',kind='line',figsize=(10,20))
        plt.xlabel('日付')
        plt.ylabel('アクセス数')
        plt.grid()
        plt.savefig(img_dir + 'access_count.png')
    
    def make_ip_count(self,rank_c):
        print('IPアドレス　　アクセス数')
        plt.clf()
        self.fpass['from_ip_address'].value_counts().sort_values(ascending=False).head(rank_c).plot(kind='bar',figsize=(10,20))
        self.fpass['from_ip_address'].value_counts().sort_values(ascending=False).to_csv('ip.csv')
        print(self.fpass['from_ip_address'].value_counts().sort_values(ascending=False).head(rank_c))
        plt.ylabel('アクセス数')
        plt.xlabel('ipアドレス')
        plt.savefig(img_dir + 'ip_address_count.png')
        
    def make_response_plot(self):
        print('ステータスコード')
        plt.clf()
        self.fpass['status_code'].value_counts().sort_values(ascending=False).to_csv('response_count.csv')
        self.fpass['status_code'].value_counts().sort_values(ascending=False).plot(kind='bar',figsize=(10,20))
        print(self.fpass['status_code'].value_counts().sort_values(ascending=False))
        plt.ylabel('頻度')
        plt.xlabel('ステータスコード')
        plt.savefig(img_dir + 'status_code.png')
        
    def make_url_plot(self,rank_c):
        print('URL')
        plt.clf()
        self.fpass['url'].value_counts().sort_values(ascending=False).head(rank_c).plot(kind='bar',figsize=(10,20))
        self.fpass['url'].value_counts().sort_values(ascending=False).to_csv(result_dir + 'url.csv')
        print(self.fpass['url'].value_counts().sort_values(ascending=False))
        plt.ylabel('頻度')
        plt.xlabel('url')
        plt.savefig(img_dir + 'url.png')
    
    def make_httpres_plot(self):
        print('HTTPレスポンス')
        plt.clf()
        self.fpass['res'].value_counts().sort_values(ascending=False).plot(kind='bar',figsize=(10,20))
        print(self.fpass['res'].value_counts().sort_values(ascending=False))
        self.fpass['res'].value_counts().sort_values(ascending=False).to_csv(result_dir + 'HTTPres.csv')
        plt.ylabel('頻度')
        plt.xlabel('res')
        plt.savefig(img_dir + 'res.png')        
    
    def save_csv(self):
        self.fpass.to_csv(result_dir + 'log_df.csv',index=False)
    
    def mung(self):
        print('process start')
        self.fpass['ymd']=self.fpass['ymd'].str.replace('[','')
        self.fpass['time']=self.fpass['time'].str.replace(']','')
        self.fpass['time']=pd.to_datetime(self.fpass['ymd'] + ' ' + self.fpass['time'],format='%Y-%m-%d %H:%M:%S+0900')
        self.fpass['ymd']=pd.to_datetime(self.fpass['ymd'],format='%Y-%m-%d')
        for i in range(0,len(self.fpass['basic64'])):
            self.fpass['basic64'][i] = base64.b64decode(self.fpass['basic64'][i]).decode()
            
        self.fpass['res']=self.fpass['HTTP']
        self.fpass['url']=self.fpass['HTTP']
        self.fpass['country'] = self.fpass['from_ip_address']
        for i in range(0,len(self.fpass['HTTP'])):
            self.fpass['res'][i] = self.fpass['HTTP'].str.split()[i][0]

        for i in range(0,len(self.fpass['from_ip_address'])):
            try:
                self.fpass['country'][i] = self.ip_dict.city(self.fpass['from_ip_address'][i]).country.names['en']
            except:
                self.fpass['country'][i] = "None"
        print('end of data mungging')
            
        return self.fpass
    
    def ip_country(self):
        print('国別集計')
        plt.clf()
        self.fpass['country'].value_counts().sort_values(ascending=False).plot(kind='bar',figsize=(15,20))
        print(self.fpass['country'].value_counts().sort_values(ascending=False))
        self.fpass['country'].value_counts().sort_values(ascending=False).to_csv(result_dir + 'country.csv')
        plt.ylabel('頻度')
        plt.xlabel('country code')
        plt.savefig(img_dir + 'country.png')   
        
if __name__ == "__main__":
    start = t.time()
    log_an = log_analytic_code('/Users/takishun/files/log20250102/log.txt','GeoLite2-City.mmdb') 
    try: 
        df = log_an.mung()
        log_an.make_access_plot()
        log_an.make_ip_count(10)
        log_an.make_url_plot(10)
        log_an.make_response_plot()
        log_an.make_httpres_plot()
        log_an.ip_country()
        log_an.save_csv()
    except:
        print('except')
    print('log_process_end: {}[sec]'.format(t.time()-start))


# In[4]:


d = pd.read_csv('log_df.csv')


# In[ ]:




