import requests
from bs4 import BeautifulSoup

def get_stops(url):
    """get all bus&tram stops with links from dpmk url in a format [link, name_of_stop]"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    options = soup.find_all('option')

    stops = []

    for option in options:
        n = option.get('value')
        if n:
            stop = [f"https://www.dpmk.sk/cp/zastavka/{n[5:]}", option.get_text().strip()]
            stops.append(stop)

    return stops

all_stops = get_stops("https://www.dpmk.sk/cp")

for stop in all_stops:
    print(stop)
# print(all_stops)