"""
this file firstly determines what type of day it is and then based on that gets all times for specific line/direction.
"""

import requests
from bs4 import BeautifulSoup
from get_lines import old_hospital_data, old_hospital_lines
import json
from datetime import date


def get_type_of_day():
    # determine whether today is a holiday, working day or free day using dpmk api and then return class based on this
    # this class is used later in times extraction
    
    url_for_type_of_day = "https://www.dpmk.sk/api/cp/today"
    type_of_day = requests.get(url_for_type_of_day).text
    determined_class = type_of_day + " table-wrapper time"
    
    return determined_class

def get_times_for_today(url, determined_class):
    # Get times based on type of day (working-days, holidays, free-days)
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
    
    return f"{hours}:{minutes}"

    
type_of_day_today = get_type_of_day()   

for line in old_hospital_lines:
    line_number = get_line_number(line)
    line_direction = get_line_direction(line)
    number_plus_direction = f'{line_number} -> {line_direction}'

    if number_plus_direction not in old_hospital_data['Stará nemocnica']['Lines']:
        old_hospital_data['Stará nemocnica']['Lines'][number_plus_direction] = {}

    old_hospital_data['Stará nemocnica']['Lines'][number_plus_direction]['Times'] = get_times_for_today(line, type_of_day_today)

# print(json.dumps(old_hospital_data, indent=4, ensure_ascii=False))

# Save the dictionary to a JSON file
with open('bus_stop_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(old_hospital_data, json_file, indent=4, ensure_ascii=False)