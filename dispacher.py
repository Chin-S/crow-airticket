#-*-coding:utf-8-*-
import downloader
import threading
import urlmanager
import handler
import time

class dispacter:
    def __init__(self,startcity,destcity,blockdate):
        self.downloader = downloader.downloader()
        self.urlmanager = urlmanager.urlmanager(startcity,destcity,blockdate)
        self.handler = handler.handler()
    def start(self): 
        while(self.urlmanager.has_uncrowedurl()):
            url = self.urlmanager.get_uncrowedurl()
            html = self.downloader.download(url)
            time = 0
            handle_result = False
            while not handle_result and time<3:
                handle_result = self.handler.handle(html)
                time += 1
if __name__ == '__main__':
    while(True):
        crow1 = dispacter('CTU','XIY','2017-02-10')
        crow2 = dispacter('NAO','XIY','2017-02-10')
        threads = []
        crow1_thread = threading.Thread(target = crow1.start())
        threads.append(crow1_thread)
        crow2_thread = threading.Thread(target = crow2.start())
        threads.append(crow2_thread)
        for t in threads:
            t.start()
        time.sleep(3600*8)
            
            

