import csv
import configparser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('config.ini')
geckodriver_path = config['WebDriver']['geckodriver_path']
service = Service(geckodriver_path) 
driver = webdriver.Firefox(service=service)
url_list = [
    'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/',
    'https://www.olx.pl/nieruchomosci/domy/sprzedaz/'
]

end_list = [['link1','link2','Tytuł','Cena','Lokalizacja','wielkosc']]

for url in url_list:
    print('$'*75)
    print(url)
    for iter in range(1,26):
        print(iter)
        driver.get(url+f"?page={iter}")
        wait = WebDriverWait(driver, 10)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        temp_list = soup.find_all('div',{'data-cy':'l-card'})
        for line in temp_list: 
            print(50*'_')
            # print(line.prettify())
            try:
                link = line.find('a')['href']
                tytul = line.find('h6').get_text()
                cena = line.find('p').get_text()
                lokalizacja = line.find('p',{'data-testid':'location-date'}).get_text()
                cena_za_metr = line.find('div',{'color':'text-global-secondary'}).get_text()
                print(link)
                print(tytul)
                print(cena)
                print(lokalizacja)
                print(cena_za_metr)
                end_list.append([url,link,tytul,cena,lokalizacja,cena_za_metr])
            except:
                print('Błąd')
                print(line.prettify())
        
with open('olx_mieszkania.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(end_list)
