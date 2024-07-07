from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time
import fake_useragent

user = fake_useragent.UserAgent().random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user}')
driver = webdriver.Chrome(options=options)


def get_city_list(link):
    try:
        city_names = []
        driver.get(url = link)
        time.sleep(2)
        btn_div = driver.find_element(By.CLASS_NAME,'RegionLabel_label___UHIA')
        btn = btn_div.find_element(By.TAG_NAME, 'svg')
        btn.click()
        time.sleep(2)
        main_page = driver.page_source
        soup = BeautifulSoup(main_page,'lxml')
        city_list = soup.find('ul',class_ = 'Autocomplete_autocomplete-suggestions__pF1oZ').find_all('li')
        for city_name in city_list:
            city_names.append(city_name.text)
        time.sleep(2)
        with open('cities.txt','w',encoding='utf-8') as file:
            for i in city_names:
                file.write(str(i) + '\n')
        driver.close()
        driver.quit()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



def get_drug_names(link):
    try:
        page_urls = []
        driver.get(url = link)
        time.sleep(2)
        btn_div = driver.find_element(By.CLASS_NAME,'RegionLabel_label___UHIA')
        btn = btn_div.find_element(By.TAG_NAME, 'svg')
        btn.click()
        time.sleep(2)
        bttn_list = driver.find_element(By.CLASS_NAME, 'Autocomplete_autocomplete-suggestions__pF1oZ')
        bttns = bttn_list.find_elements(By.TAG_NAME, 'li')
        for i in range(len(bttns)):
            bttn_list = driver.find_element(By.CLASS_NAME, 'Autocomplete_autocomplete-suggestions__pF1oZ')
            bttns = bttn_list.find_elements(By.TAG_NAME, 'li')
            bttn = bttns[i]
            bttn.click()
            print(1)
            time.sleep(3)
            local_url = driver.find_element(By.CLASS_NAME, 'Container_container__f9MJQ').find_element(By.TAG_NAME,'div').find_elements(By.TAG_NAME,'a')[3].get_attribute('href')
            page_urls.append(local_url)
            print(2)
            time.sleep(3)
            btn_div = driver.find_element(By.CLASS_NAME,'RegionLabel_label___UHIA')
            btn = btn_div.find_element(By.TAG_NAME, 'svg')
            btn.click()
            time.sleep(3)
        print(page_urls)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()




def main():
    # get_city_list('https://zdravcity.ru/')
    get_drug_names('https://zdravcity.ru/')

if __name__ == '__main__':
    main()
