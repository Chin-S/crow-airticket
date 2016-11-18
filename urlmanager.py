#-*-coding:utf-8-*-
import datetime
# https://touch.qunar.com/h5/flight/flightlist?startCity=%E5%8C%97%E4%BA%AC&&destCity=%E4%B8%8A%E6%B5%B7&destCode=&startDate=2016-11-19&backDate=&flightType=oneWay
class urlmanager:
    base = 'https://touch.qunar.com/h5/flight/flightlist?flightType=oneway&'
    start_city = None
    dest_city = None
    block_date = blockdate
    urls = set()
    def __init__(self,startcity,destcity,blockdate):
        start_city = startcity
        dest_city = destcity
        block_date = datetime.time.strptime(blockdate,'%Y-%m-%d')
        creat_urls()
    def creat_urls(self):
        today = datetime.date.today
        dest_date = today
        while(dest_date != block_date):
            dest_datestr = dest_date.strftime('%Y-%m-%d')
            url = base+'startCity=%s&'%destcity+'destCity=%s&'%destcity+'startDate%s&'%dest_datestr
            urls.add(url)
            dest_date = dest_date+datetime.timedelta(1)
    def has_uncrowedurl(self):
        return len(urls)
    def get_uncrowedurl(self):
        if has_uncrowedurl:
            return urls.pop()
        return None
        

            
        

