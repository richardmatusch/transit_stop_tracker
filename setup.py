from bs4 import BeautifulSoup
import requests
import json


def get_stops():
    """get all bus&tram stops with links from dpmk url in a format [link, name_of_stop]"""
    response = requests.get("https://www.dpmk.sk/cp")
    soup = BeautifulSoup(response.content, 'html.parser')
    options = soup.find_all('option')

    stops = []

    for option in options:
        n = option.get('value')
        if n:
            stop = [f"https://www.dpmk.sk/cp/zastavka/{n[5:]}", option.get_text().strip()]
            stops.append(stop)

    return stops

def choose_stop(stops):
    print("Available stops for tracking:\n")
    for i, stop in enumerate(stops, 1):
            print(f"{i} - {stop[1]}")
            
    selected = input("\nPlease enter number of chosen stop: ")
    return selected
    
def generate_config(stop_id):
    stop_link = all_stops[int(stop_id) - 1][0]
    stop_name = all_stops[int(stop_id) - 1][1]
    
    config = {
        "tracked_stop": {
            "name": stop_name,
            "link": stop_link
        }
    }
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    print(f"\nConfig saved to config.json. Tracked stop: {stop_name}")
      
            
all_stops = get_stops()
chosen_stop = choose_stop(all_stops)
generate_config(chosen_stop)
