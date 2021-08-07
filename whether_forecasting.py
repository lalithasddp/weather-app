

import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/search?q=weather bangalore"

html = requests.get(url).content
response_data = BeautifulSoup(html, 'html.parser')

#print(response_data)

temp = response_data.find('div', attrs= {'class': 'BNeawe iBp4i AP7Wnd'}).text
day = response_data.find('div', attrs= {'class': 'BNeawe tAd8D AP7Wnd'}).text
print(temp)
print(day)