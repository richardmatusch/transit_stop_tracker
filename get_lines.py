"""
this file gets links for all buses/trams in all directions for a specific stop.
in this case i'm hardcoding old hospital because this project is about this stop only so far.
"""

import requests
from bs4 import BeautifulSoup


def get_links_from_stop(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []

    table = soup.find_all('tr')
    for i in table:
        a = i.find('a')
        if a:
            link = f"https://www.dpmk.sk{a.get('href')}"
            if link:
                links.append(link)

    return links


# old hospital tram/bus stop url
url = 'https://www.dpmk.sk/cp/zastavka/184'

old_hospital_data = {
    "Stará nemocnica": {
        "Lines":{
            
        }
    }
}

old_hospital_lines = get_links_from_stop(url)

