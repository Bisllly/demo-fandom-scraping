import requests
from bs4 import BeautifulSoup
try:
    import brotli
except ImportError:
    brotli = None


with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9"
    }

response =  se.get('https://slamdunk.fandom.com/wiki/Hanamichi_Sakuragi')

soup = BeautifulSoup(response.content, 'html.parser')

s = soup.find('div', id='content')
content = s.find_all('p')

print(content)