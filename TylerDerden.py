import re
import requests
from bs4 import BeautifulSoup
import json

with open('index0.html') as file:
    code = file.read()
soup = BeautifulSoup(code,'lxml')

data = []

celebrates_names_list = soup.find_all('h3', class_ = 'margin-top-0 margin-bottom-5 card-title')
for i in range(len(celebrates_names_list)):
    festival_name = (celebrates_names_list[i]).text
    for l in range(len((soup.find_all('div', class_ = 'pad-15 p-9pt tc-white')[i]).find_all('p'))):
        celebrates_dates_list = soup.find_all('div', class_ = 'pad-15 p-9pt tc-white')[i].find_all('p')[l].find_all('span')
    # print(festival_name)
        print(celebrates_dates_list[0])
#soup.find('p', class_ = 'details-list  margin-bottom-0').find('span',class_ = 'icon-newcal list-icon').find_next_sibling('span').text
