class log_analytic_code:
    def __init__(self,fpass):
        import pandas as pd
        import matplotlib.pyplot as plt
        import warnings
        import base64
        warnings.simplefilter('ignore')
        %matplotlib inline
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
