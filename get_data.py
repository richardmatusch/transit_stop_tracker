"""
this file uses config.json generated from setup.py to extract times for
all lines in every direction for specific stop. this data is then saved
as data.json
"""

from bs4 import BeautifulSoup
import requests
import json


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
    
    print(f"found lines in '{stop_name}': {len(links)}\n")
    return links

def get_type_of_day():
    # determine type of day according to dpmk api
    url_for_type_of_day = 'https://www.dpmk.sk/api/cp/today'
    type_of_day = requests.get(url_for_type_of_day).text
    determined_class = type_of_day + ' table-wrapper time'

    print(f"determined type of day: '{type_of_day}'\n")
    return determined_class

def get_times_for_today(url, determined_class):
    # get times based on type of day (working-days, holidays, free-days)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    day_today = soup.find('div', class_=determined_class)
    if not day_today:
        return []

    time_spans = day_today.find_all('span', attrs={'data-time': True})
    data_times = [convert_data_time_to_time(span['data-time']) for span in time_spans if 'data-time' in span.attrs]

    return data_times

def get_line_number(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    h1 = soup.find('h1')
    if not h1:
        return None

    span = h1.find('span')
    if not span:
        return None

    return span.get_text()

def get_line_direction(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong = soup.find('strong', class_='to')
    if not strong:
        return None

    return strong.get_text()

def convert_data_time_to_time(time_str):
    time_str = time_str.zfill(4)
    hours = time_str[:2]
    minutes = time_str[2:]

    return f'{hours}:{minutes}'


with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

stop_link = config['tracked_stop']['link']
stop_name = config['tracked_stop']['name']

stop_lines = get_lines_from_stop(stop_link)
type_of_day_today = get_type_of_day()
data = {
    'stop_name': stop_name,
    'stop_link': stop_link,
    'lines_and_directions': {
    }
}

for line in stop_lines:
    line_and_direction = f'{get_line_number(line)} -> {get_line_direction(line)}'

    if line_and_direction not in data['lines_and_directions']:
        print(f"getting times for: '{line_and_direction}'...")
        data['lines_and_directions'][line_and_direction] = {}
        data['lines_and_directions'][line_and_direction]['Times'] = get_times_for_today(line, type_of_day_today)

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
    print(f"\nall lines and times for '{stop_name}' were saved into 'data.json' succesfully")
