import sendemail
class handler:
    def __init__(self):
        self.sendemail = sendemail.sendemail()
        self.data = []
        self.price = 500
    def collect(self,data):
        self.data.append(data)
    def handle(self):
        for items in self.data:
            for item in items:
                print item['from_time']+item['from_place']
                print item['to_time']+item['to_place']
                print item['price']+item['moreinfo']+item['company']
