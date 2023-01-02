from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(url)
if not response.status_code == 200:
    print('An error has occurred.')
    exit()
else:
    print('Success!')
    soup = BeautifulSoup(response.text, 'html5lib')
    # get all heading h3
    headings_3 = soup.find_all('h3')
    print("Headings 3:")
    for i in headings_3:
        print(i.text)

    # get all links
    links = soup.find_all('a')
    print("Links:")
    for i in links:
        print(f'{i.text} 🔗 {i.get("href")}')