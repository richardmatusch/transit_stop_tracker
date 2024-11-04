import requests
from bs4 import BeautifulSoup

url = 'https://www.dpmk.sk/cp'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
options = soup.find_all('option')

stops = []

for option in options:
    n = option.get('value')
    if n:
        stop = [f"https://www.dpmk.sk/cp/zastavka/{n[5:]}", option.get_text().strip()]
        stops.append(stop)

for stop in stops:
    print(stop)