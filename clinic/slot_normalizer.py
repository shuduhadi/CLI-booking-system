import datetime
from clinic.config import SLOT_MINS

SLOT_LENGTH = datetime.timedelta(minutes=SLOT_MINS)


def _parse_time(value):
    if "dateTime" in value:
        return datetime.datetime.fromisoformat(value["dateTime"])
    return None


def normalize_events(student_events, clinic_events):
    slots = {}

    def mark(events, key):
        for event in events:
            start = _parse_time(event["start"])
            end = _parse_time(event["end"])

            if not start or not end:
                continue

            current = start
            while current < end:
                slot_end = current + SLOT_LENGTH
                slot_key = (current.date(), current.time())

                if slot_key not in slots:
                    slots[slot_key] = {
                        "date": current.date().isoformat(),
                        "start": current.strftime("%H:%M"),
                        "end": slot_end.strftime("%H:%M"),
                        "student_busy": False,
                        "clinic_busy": False,
                    }

                slots[slot_key][key] = True
                current = slot_end

    mark(student_events, "student_busy")
    mark(clinic_events, "clinic_busy")

    result = []
    for slot in slots.values():
        if slot["student_busy"] and slot["clinic_busy"]:
            slot["status"] = "blocked"
        elif slot["student_busy"]:
            slot["status"] = "student_busy"
        elif slot["clinic_busy"]:
            slot["status"] = "clinic_busy"
        else:
            slot["status"] = "free"

        result.append(slot)

    return sorted(result, key=lambda s: (s["date"], s["start"]))
