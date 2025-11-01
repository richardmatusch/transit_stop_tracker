from bs4 import BeautifulSoup
import requests
import json
from datetime import date


def get_lines_from_stop(url):
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
    
def get_type_of_day():
    """
    determine whether today is a holiday, working day or free day according to
    dpmk api and then return corresponding class. this class is used later in times extraction
    """
    
    url_for_type_of_day = "https://www.dpmk.sk/api/cp/today"
    type_of_day = requests.get(url_for_type_of_day).text
    determined_class = type_of_day + " table-wrapper time"
    
    return determined_class


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

stop_link = config["tracked_stop"]["link"]

stop_lines = get_lines_from_stop(stop_link)
print(stop_lines)
