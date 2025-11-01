import json
from get_stops import all_stops

def choose_stop(stops):
    for i, stop in enumerate(stops, 1):
            print(f"{i} - {stop[1]}")
            
    selected = input("Please choose stop:")
    return selected
    
def generate_config(stop_id):
    config = {"tracked_stop": stop_id}
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    print(f"Config saved to config.json. Tracked stops: {stop_id}")
            
chosen_stop = choose_stop(all_stops)
generate_config(chosen_stop)
