from bs4 import BeautifulSoup
import re
class myparser:
    def parse(self,content,url):
        if len is None:
           return None
        data = []
        soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
        pattern_from_time = re.compile(r'<p class="from-time time-font">(.*?)</p>')
        pattern_from_place = re.compile(r'<p class="from-place ellipsis">(.*?)</p>')
        pattern_to_time = re.compile(r'<p class="to-time time-font">(.*?)</p>')
        pattern_to_place = re.compile(r'<p class="to-place ellipsis">(.*?)</p>')
        pattern_company = re.compile(r'<span class="company.*?">(.*?)</span>')
        pattern_price = re.compile(r'<p class="price-info">.*?(\d{2,5}).*?</p>')
        pattern_moreinfo = re.compile(r'<p class="more-info">(.*?)</p>')
        row_items=soup.find_all('li',class_='list-row item')
        for item in row_items:
            print item
            temp = {}
            item = str(item)
            temp['from_time'] = pattern_from_time.search(item).group(1)
            temp['to_time'] = pattern_to_time.search(item).group(1)
            temp['from_place'] = pattern_from_place.search(item).group(1)
            temp['to_place'] = pattern_to_place.search(item).group(1)
            temp['company'] = ''.join(pattern_company.findall(item)) 
            temp['price'] = pattern_price.search(item).group(1)
            temp['moreinfo'] = pattern_moreinfo.search(item).group(1)
            temp['url'] = url
            data.append(temp)
        return data
        
        
