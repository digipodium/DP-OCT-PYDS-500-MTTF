import requests

url = 'http://www.google.com/search?q=python'
response = requests.get(url)
if response.status_code == 200:
    print('Success!')
    print(response.text)
else:
    print('An error has occurred.')
