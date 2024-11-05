import requests
from bs4 import BeautifulSoup

url = 'https://www.dpmk.sk/cp/linka/40001/184/14/1'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
spans = soup.find_all('span')

for span in spans:
    data_time = span.get('data-time')
    if data_time:
        print(f"{data_time[:-2]}:{data_time[-2:]}")