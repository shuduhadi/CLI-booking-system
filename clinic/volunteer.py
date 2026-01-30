import datetime

VOLUNTEER_AVAILABILITY = {
    0: [('12:00', '16:00')],
    1: [('12:00', '16:00')],
    2: [('12:00', '16:00')],
    3: [('12:00', '16:00')],
    4: [('12:00', '16:00')],
}

def is_volunteer_available(date_str, start_time_str, end_time_str):
    date = datetime.date.fromisoformat(date_str)
    weekday = date.weekday()

    if weekday not in VOLUNTEER_AVAILABILITY:
        return False
    
    start = datetime.datetime.strptime(start_time_str, "%H:%M").time()
    end = datetime.datetime.strptime(end_time_str, "%H:%M").time()

    for window_start, window_end in VOLUNTEER_AVAILABILITY[weekday]:
        ws = datetime.datetime.strptime(window_start, "%H:%M").time()
        we = datetime.datetime.strptime(window_end, "%H:%M").time()

        if start >= ws and end <= we:
            return True
    return False