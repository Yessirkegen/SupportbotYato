import requests
from bs4 import BeautifulSoup

def searcher():
    links=[]
    url = 'https://www.pinterest.ru/pin/5418462043096747/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    #print(soup.prettify())
    pins= soup.findAll('img', class_='hCL kVc L4E MIw')
    for i in pins:
       links.append(i['src'])
    return links