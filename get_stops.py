"""
this file gets all stops with links and names into a list. there is no really automated use for it yet.
im just using stará nemocnica stop manually from the list.
"""

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

"""
counter = 1
for stop in all_stops:
    print(f"stop {counter}: {stop}")
    counter += 1
    
print(all_stops[208])
"""