import requests
from bs4 import BeautifulSoup
import json

# determine type of day
url_for_type_of_day = "https://www.dpmk.sk/api/cp/today"
type_of_day = requests.get(url_for_type_of_day).text
determined_class = type_of_day + " table-wrapper time"

# get times based on type of day (working-days, holidays, free-days)
def get_times_for_today(url, determined_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    day_today = soup.find('div', class_=determined_class)
    time_spans = day_today.find_all('span', attrs={'data-time': True}) #type: ignore
    data_times = [span['data-time'] for span in time_spans]
    
    return data_times
    
todays_times = get_times_for_today("https://www.dpmk.sk/cp/linka/40001/184/14/1", determined_class)
print(todays_times)