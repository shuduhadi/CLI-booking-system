import datetime

def display_events(events):
    if not events:
        print('No events found for the next 7 days.')
        return
    current_day = None
    
    for event in events:
        start_raw = event['start'].get(
            'dateTime',
            event['start'].get('date')
        )
        start = datetime.datetime.fromisoformat(
            start_raw.replace('Z', '+00:00')
        )
        date_str = start.strftime("%Y-%m-%d")
        time_str = start.strftime('%H:%M')

        if date_str != current_day:
            print(f"\n📅 {date_str}")
            current_day = date_str

        summary = event.get('summary', 'No title')
        print(f"  {time_str} - {summary}")