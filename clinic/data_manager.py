import json
import datetime
from pathlib import Path

from clinic.config import CACHE_FILE, CACHE_TTL_SECONDS


def load_cache():
    cache_path = Path(CACHE_FILE)

    if not cache_path.exists():
        return None

    with open(cache_path, "r") as f:
        return json.load(f)


def save_cache(student_events, clinic_events):
    cache_data = {
        "last_updated": datetime.datetime.now(
            tz=datetime.timezone.utc
        ).isoformat(),
        "student": student_events,
        "clinic": clinic_events,
    }
    with open(CACHE_FILE, "w") as f:
        json.dump(cache_data, f, indent=2)


def cache_is_fresh(cache_data):
    last_updated = datetime.datetime.fromisoformat(
        cache_data["last_updated"]
    )
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    age = now - last_updated
    return age.total_seconds() < CACHE_TTL_SECONDS
