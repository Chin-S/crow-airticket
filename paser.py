from bs4 import BeautifulSoup
import re
class parser:
    def parse(html):
        if len(html) == 0:
            return None
        data = set()
        soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')

        
        
