#-*-coding:utf-8-*-
import myparser
import downloader
import threading
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
            html = self.downloader.download(url)
            content = self.myparser.parse(html,url)
            self.handler.handle(content)
if __name__ == '__main__':
    while(True):
        crow1 = dispacter('成都','西安','2017-02-10')
        crow2 = dispacter('南充','西安','2017-02-10')
        threads = []
        crow1_thread = threading.Thread(target = crow1.start())
        threads.append(crow1_thread)
        crow2_thread = threading.Thread(target = crow2.start())
        threads.append(crow2_thread)
        for t in threads:
            t.start()
        time.sleep(3600*8)
            
            

