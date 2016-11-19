#-*-coding:utf-8-*-
import myparser
import downloader
import urlmanager
import handler
import time

class dispacter:
    def __init__(self,startcity,destcity,blockdate):
        self.downloader = downloader.downloader()
        self.myparser = myparser.myparser()
        self.urlmanager = urlmanager.urlmanager(startcity,destcity,blockdate)
        self.handler = handler.handler()
    def start(self): 
        while(self.urlmanager.has_uncrowedurl()):
            url = self.urlmanager.get_uncrowedurl()
            print url
            html = self.downloader.download(url)
            content = self.myparser.parse(html)
            self.handler.collect(content)
        self.handler.handle()
if __name__ == '__main__':
    while(True):
        dispacther = dispacter('成都','西安','2017-02-10')
        dispacther.start()
        time.sleep(3600*8)
            
            

