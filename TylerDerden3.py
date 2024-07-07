import re
from bs4 import BeautifulSoup
import json
import requests
import random
import fake_useragent
import time

user = fake_useragent.UserAgent().random
headers = {'iser-agent':user}

data = []

item_links = set()
for i in range(0,17):
    link = f'https://welcome.mosreg.ru/places/museums?page={i}'
    req = requests.get(link, headers = headers).text
    with open('museum_code.html','w',encoding='utf-8') as file:
        file.write(req)
    with open('museum_code.html',encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    cards_list = soup.find('div',class_ = 'p-three-list').find_all('div', class_ = 'p-three-card')
    for item in cards_list:
        item_link = item.find('a', class_ = 'w_newsList__item-box').get('href')
        item_links.add('https://welcome.mosreg.ru'+item_link)
print(len(item_links))
for local_link in item_links:
    req_local = requests.get(local_link, headers = headers).text
    with open('museum_code_local.html','w',encoding='utf-8') as file:
        file.write(req_local)
    with open('museum_code_local.html',encoding='utf-8') as file:
        src_local = file.read()
    soup_local = BeautifulSoup(src_local,'lxml')
    name = soup_local.find('div',class_ = 'item-page-name-block').find('h1').text
    adress = soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li')[0].find('a').text
    rastoyanie = soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li')[1].find('span')
    print(name)
    if rastoyanie is None:
        rastoyanie = 'Не указано'
    else:
        rastoyanie = rastoyanie.text
    if len(soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li'))<3:
        phone = soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li')[1]
        if phone is None:
            phone = 'Не указан'
        else:
            phone = phone.find('a').text
        website = soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li')[1]
        if website is None:
            website = 'Не указан'
        else:
            website = website.find('a', class_ = 'web__link')
            if website is None:
                website = 'Не указан'
            else:
                website = website.get('href')
    else:
        phone = soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li')[2]
        if phone is None:
            phone = 'Не указан'
        else:
            phone = phone.find('a').text
        website = soup_local.find('div',class_ = 'rs-three-left').find('ul').find_all('li')[2]
        if website is None:
            website = 'Не указан'
        else:
            website = website.find('a', class_ = 'web__link')
            if website is None:
                website = 'Не указан'
            else:
                website = website.get('href')
    local_data = {
        'Название музея': name,
        'Адрес': adress,
        'Расстояние до Москвы': rastoyanie,
        'Телефон': phone,
        'Сайт': website
    }   
    print(local_data)
    data.append(local_data)
with open('museums_data.json','w',encoding='utf-8') as json_file:
    json.dump(data,json_file, indent=4,ensure_ascii=False)
