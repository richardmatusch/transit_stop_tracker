import requests
from bs4 import BeautifulSoup

# url should be fetched from html file index.html
url = 'https://www.dpmk.sk/cp/zastavka/184'

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

old_hospital = get_links_from_stop(url)

print(old_hospital)