import requests
from bs4 import BeautifulSoup
import time

requests.packages.urllib3.disable_warnings()

dataType = 'pdf'
google_url = "https://www.google.com.tw/search"
my_params = {'q': 'what want to find' + ' filetype:'+dataType,'start':0}              #一頁10個result，start設10的倍數
headers = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}

r = requests.get(google_url, params = my_params,headers=headers)


soup = BeautifulSoup(r.text, 'html.parser')
items = soup.select('div.r>a')

requests.adapters.DEFAULT_RETRIES = 5
for i in items:
    # 標題
    title = i.next.next.text
    print("標題：" + title)
    # 網址
    url = i.get('href')
    print("網址：" + url)

    s = requests.session()
    s.keep_alive = False
    x = s.get(url,headers=headers,verify=False)
    #print(x.content)
    with open(title + '.' + dataType,'wb') as f:   
        f.write(x.content)
    #time.sleep(2)