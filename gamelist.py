from bs4 import BeautifulSoup
import urllib.request
import requests as re
import json

#page max - 32 on site xbox360

def parse(pageCurrent = 1, PageSize = 30):
    listArr = {}
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    url = "http://marketplace.xbox.com/ru-RU/Games/Xbox360Games?PageSize="+str(PageSize)+"&sortby=BestSelling&Page="+str(pageCurrent)
    req = urllib.request.Request(url, None, headers)
    page = urllib.request.urlopen(req)
    
    soup = BeautifulSoup(page.read(), 'html.parser')
    
    list = soup.find('ol', class_='ProductResults GameTiles')
    
    i = 0;
    for val in list.select('h2 a',limit=PageSize):
        urlIn = "http://marketplace.xbox.com" + val['href']
        req = urllib.request.Request(urlIn, None, headers)
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
        
    return listArr

if __name__ == "__main__":
    list = {}
    for z in range(1, 3): #1, 2 = parse 1 page OR 1, 3 = parse 2 page
        list[z] = parse(z)
        
    f = open('text2.txt', 'w')
    f.write(json.dumps(list))
    f.close()
    
#    fList = {}
#    i = 1
#    for ls in list:
#        kk = 1
#        for ls in list[i]:
#            fList[kk] = list[i][kk]
#            kk += 1
#        i += 1
#        
#    
#    print('----------------------')
#    i = 1
#    for val in fList:
#        print(fList[i]['name'])
#        print(fList[i]['price'])
#        print('----------------------')
#        i += 1
        