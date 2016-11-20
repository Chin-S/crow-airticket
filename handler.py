#-*-coding:utf-8-*-
import time
import time
import sendemail
class handler:
    def __init__(self):
        self.emailutil = sendemail.sendemail()
        self.price = 150
        self.to = [
                'rikeandmorty@sina.com',
                '1164010996@qq.com'
                ]
    def handle(self,data):
        for item in data:
            if int(item['price']) < self.price:
                content = self.get_content(item)
                self.emailutil.send('it works!!!',content,self.to)
                time.sleep(60*60*10)
    def get_content(self,item):
        from_place = item['from_place']
        to_place = item['to_place']
        from_time = item['from_time']
        to_time = item['to_time']
        flight_info = item['company']
        price = item['price']
        moreinfo = item['moreinfo']
        url = item['url']
        content = '<h3>air ticket</h3><table style="border:1px solid black"><tr><th>出发</th><th>到达</th><th>价格</th><th>航班</th><th>更多</th></tr><tr><td>%s%s</td><td>%s%s</td><td>%s</td><td>%s</td><td>%s</td></tr></table><br/><a href="%s">详情&gt;&gt;&gt;</a>'%(from_time,from_place,to_time,to_place,price,flight_info,moreinfo,url)
        return content


        
            


                    
