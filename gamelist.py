from bs4 import BeautifulSoup
import urllib.request
import requests as re

listArr = {}
PageSize = 30
Page = 1

if __name__ == "__main__":
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = { 'User-Agent' : user_agent }
    url = "http://marketplace.xbox.com/ru-RU/Games/Xbox360Games?PageSize="+str(PageSize)+"&Page="+str(Page)
    req = urllib.request.Request(url, None, headers)
    page = urllib.request.urlopen(req)
    
    #print(page.read())
    
    soup = BeautifulSoup(page.read(), 'html.parser')
    
    list = soup.find('ol', class_='ProductResults GameTiles')
    #print(list.select('h2 a'))
    i = 0;
    for val in list.select('h2 a',limit=PageSize):
        urlIn = "http://marketplace.xbox.com" + val['href']
        req = urllib.request.Request(urlIn, None, headers)
        #p = re.get(urlIn)
        p = urllib.request.urlopen(req)
        s = BeautifulSoup(p.read(), 'html.parser')
        price = s.find('span', class_='SilverPrice ProductPrice', text=True)
        
        if price is None:
            sPrice = ''
        else:
            sPrice = price.string
        
        i += 1
        listArr[i] = {
        #'href': val['href'],
        'name': val['title'],
        'price': sPrice
        }

    #print(listArr[1]['name'])
    print('----------------------')
    
    i = 1
    for val in listArr:
        print(listArr[i]['name'])
        print(listArr[i]['price'])
        print('----------------------')
        i += 1
        