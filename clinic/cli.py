import argparse
from clinic.calendar_api import fetch_next_7_days
from clinic.config import STUDENT_CALENDAR_ID, CLINIC_CALENDAR_ID
from clinic.data_manager import load_cache, save_cache, cache_is_fresh
from clinic.display import display_events
from clinic.slot_normalizer import normalize_events


def view_calendars():
    cache = load_cache()

    if cache and cache_is_fresh(cache):
        print("Using cached calendar data.")
        students_events = cache['student']
        clinic_events = cache['clinic']
    else:
        print('Downloading calendar data from Google...')
        students_events = fetch_next_7_days(STUDENT_CALENDAR_ID)
        clinic_events = fetch_next_7_days(CLINIC_CALENDAR_ID)
        save_cache(students_events, clinic_events)

    print("\n=== STUDENT CALENDAR ===")
    display_events(students_events)

    print('\n=== CLINIC CALENDAR ===')
    display_events(clinic_events)


def view_slots():
    events = fetch_next_7_days()
    slots = normalize_events(events, "student")

    for slot in slots:
        print(
            f"{slot['date']} | {slot['start']}–{slot['end']} | {slot['calendar']} | {slot['status']}"
        )

def main():
    parser = argparse.ArgumentParser(
        description="Clinic Booking System"
    )
    parser.add_argument(
        'command',
        choices=['view','slots'],
        help='Command to run'
    )
    args = parser.parse_args()
    if args.command == 'view':
        view_calendars()
    elif args.command == 'slots':
        view_slots()

if __name__ == '__main__':
    main()