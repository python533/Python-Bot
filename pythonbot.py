import requests

from bs4 import BeautifulSoup

r=requests.get('')
soup=BeautifulSoup(r.text,'html.parser')

kayitlar=soup.find_all("img",{"class":""})

for  kayit in kayitlar:
    print(kayit)
