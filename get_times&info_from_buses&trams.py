import requests
from bs4 import BeautifulSoup

url = 'https://www.dpmk.sk/cp/linka/40001/184/14/1'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

bus_or_tram_number = soup.find('h1').find('span').get('class')
bus_or_tram = ''
# start extracting relevant data from bus/tram...


print(bus_or_tram_number)
print(bus_or_tram)


"""
for span in spans:
    data_time = span.get('data-time')
    if data_time:
        print(f"{data_time[:-2]}:{data_time[-2:]}")
"""