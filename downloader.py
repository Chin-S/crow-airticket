import urllib2
class downloader:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    def download(self,url):
        if url is None:
            print('error url is empty')
            return None
        request = urllib2.Request(url)
        request.add_header('User-Agent',self.user_agent)
        try:
            response = urllib2.urlopen(request,timeout=20)
            if response.getcode() != 200:

                print('%s failed'%url)
                return None
            html = response.read()
            return html
        except Exception as e:
            print e.as_string()
            pass
