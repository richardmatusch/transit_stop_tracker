"""
this file firstly determines what type of day it is and then based on that gets all times for specific line/direction.
"""

import requests
from bs4 import BeautifulSoup
from get_lines import old_hospital_lines


def get_type_of_day():
    # determine whether today is a holiday, working day or free day using dpmk api and then return class based on this
    # this class is used later in times extraction
    
    url_for_type_of_day = "https://www.dpmk.sk/api/cp/today"
    type_of_day = requests.get(url_for_type_of_day).text
    determined_class = type_of_day + " table-wrapper time"
    
    return determined_class


def get_times_for_today(url, determined_class):
    # get times based on type of day (working-days, holidays, free-days)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    day_today = soup.find('div', class_=determined_class)
    time_spans = day_today.find_all('span', attrs={'data-time': True})
    data_times = [span['data-time'] for span in time_spans]
    
    return data_times
    
    
def get_line_number(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    line_number = soup.find('h1').find('span').get_text()
  
    return line_number
    
    
def get_line_direction(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    line_direction = soup.find('strong', class_='to').get_text()
    
    return line_direction
    

lines_data =  {}

type_of_day_today = get_type_of_day()   

first_line = old_hospital_lines[0]

line_number = get_line_number(first_line)
line_direction = get_line_direction(first_line)
line_times = get_times_for_today(first_line, type_of_day_today)

print(line_number)
print(line_direction)
print(line_times)