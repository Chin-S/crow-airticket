#-*-coding:utf-8-*-
import time
import sendemail
import json 
import sys
class handler:
    def __init__(self):
        self.emailutil = sendemail.sendemail()
        self.price = 200
        self.to = [
                'rikeandmorty@sina.com',
                '1164010996@qq.com'
                ]
        reload(sys)
        sys.setdefaultencoding('utf-8')
    def handle(self,data):
        if len(data)<=0:
            print 'thire is nothing in data'
            return False
        data = json.loads(data,encoding='utf-8')
        if data['state'] != 100:
            print 'something wrong'
            return False
        for item in data['flightinfo']:
            if int(item['cabins'][0]['clientTicketPrice']) < self.price:
                content = self.get_content(item)
                self.emailutil.send('it works!!!',content,self.to)
        time.sleep(1)
        return True
    def get_content(self,item):
        from_time = item['flyOffTime']
        from_place = item['originAirportShortName']
        from_port = item['boardPoint']
        to_time = item['arrivalTime']
        to_place = item['arriveAirportShortName']
        to_port = item['offPoint']
        air_company = item['airCompanyName']
        air_code = item['flightNo']
        air_type = item['ACPlaneType']
        price = item['cabins'][0]['clientTicketPrice']
        begin_city = item['originAirportCode']
        dest_city = item['arriveAirportCode']
        start_date = from_time.split(' ')[0]
        url = 'http://m.ly.com/flightnew/%s_%s.html?refid=4140683&flyofftime=%s'%(begin_city,dest_city,start_date)
        content = '<h3>air ticket</h3><hr><table style="width:800px;border:1px solid black"><tr><th>出发</th><th>到达</th><th>价格</th><th>航班</th></tr><tr><td>%s%s%s</td><td>%s%s%s</td><td style="color:green;">%s</td><td>%s%s%s</td></tr></table><br/><a href="%s">详情&gt;&gt;&gt;</a>'%(from_time,from_place,from_port,to_time,to_place,to_port,price,air_company,air_code,air_type,url)
        return content




                    
