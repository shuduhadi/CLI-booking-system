import datetime

SLOT_LENGTH = datetime.timedelta(minutes=30)

def normalize_event(event, calendar_name):
    start_str = event['start'].get('dateTime')
    end_str = event['end'].get('dateTime')

    if not start_str or not end_str:
        return []
    
    start = datetime.datetime.fromisoformat(start_str)
    end = datetime.datetime.fromisoformat(end_str)
    slots = []
    current = start

    while current < end:
        slot_end = min(current + SLOT_LENGTH, end)
        slots.append({
            'date': current.date().isoformat(),
            'start': current.time().strftime('%H:%M'),
            'end': slot_end.time().strftime('%H:%M'),
            'calendar': calendar_name,
            'status': "busy"
        })
        current = slot_end
    return slots

def normalize_events(events, calendar_name):
    all_slots = []
    for event in events:
        all_slots.extend(normalize_event(event, calendar_name))
    return all_slots