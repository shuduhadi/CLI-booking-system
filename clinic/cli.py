import argparse
from clinic.calendar_api import fetch_next_7_days
from clinic.data_manager import load_cache, save_cache, cache_is_fresh
from clinic.display import display_events

def view_calendars():
    cache = load_cache()
    if cache and cache_is_fresh(cache):
        events = cache['events']
        print("Using cached calendar data.")
    else:
        print('Downloading calendar data from Google...')
        events = fetch_next_7_days()
        save_cache(events)

    display_events(events)

def main():
    parser = argparse.ArgumentParser(
        description="Clinic Booking System"
    )
    parser.add_argument(
        'command',
        choices=['view'],
        help='Command to run'
    )
    args = parser.parse_args()
    if args.command == 'view':
        view_calendars()

if __name__ == '__main__':
    main()