import requests
from bs4 import BeautifulSoup

url = 'https://www.dpmk.sk/cp'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
options = soup.find_all('option')

print(options)
