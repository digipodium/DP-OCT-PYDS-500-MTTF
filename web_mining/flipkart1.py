from bs4 import BeautifulSoup
import requests 

url = 'https://www.flipkart.com/search?q=bags'

page = requests.get(url)
if not page.status_code == 200:
    print('An error has occurred.')
    exit()
soup = BeautifulSoup(page.text, 'html5lib')

items = soup.find_all('div', class_='_2B099V')
for item in items:
    name = item.find('a').text
    price = item.find('div', class_='_30jeq3').text
    print(name, price)
