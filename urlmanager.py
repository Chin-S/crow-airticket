#-*-coding:utf-8-*-
import datetime
import time
class urlmanager:
    def __init__(self,startcity,destcity,blockdate):
        self.base = 'http://m.ly.com/flightnew/json/firstflightlist.html?'
        self.start_city = startcity
        self.dest_city = destcity
        self.block_date = datetime.datetime.strptime(blockdate,'%Y-%m-%d').date()
        self.urls = set()
        self.creat_urls()
    def creat_urls(self):
        today = datetime.date.today
        start_date = today()
        print start_date
        print self.block_date
        while(start_date != self.block_date):
            date_str = start_date.strftime('%Y-%m-%d')
            url = self.base+'oc=%s&'%self.start_city+'ac=%s&'%self.dest_city+'arrt=%s'%date_str
            self.urls.add(url)
            start_date = start_date+datetime.timedelta(1)
    def has_uncrowedurl(self):
        return len(self.urls)>0
    def get_uncrowedurl(self):
        if self.has_uncrowedurl():
            return self.urls.pop()
        return None
        

            
        

