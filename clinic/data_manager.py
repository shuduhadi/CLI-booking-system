import json
import os
import datetime

DATA_FILE = 'calendar_cache.json'

def load_cache():
    if not os.path.exists(DATA_FILE):
        return None
    
    with open(DATA_FILE, 'r') as file:
        return json.load(file)
    
def save_cache(events):
    data = {
        'last_updated': datetime.datetime.now(
            tz=datetime.timezone.utc
        ).isoformat(),
        'events': events,
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def cache_is_fresh(cache_data):
    last_updated = datetime.datetime.fromisoformat(cache_data['last_updated'])
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    return last_updated.date() == now.date()