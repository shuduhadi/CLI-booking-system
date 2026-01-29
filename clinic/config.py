"""
Central configuration for the clinic booking system.
"""
## Google Calendar
STUDENT_CALENDAR_ID = 'primary'

CLINIC_CALENDAR_ID = (
    "c_2b0ada51d2c238b141655269e3f369b9897d3b1b654191e53db0e5bf4e3631f9@group.calendar.google.com"
)

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'secrets/credentials.json'

##APP RULES:
DAYS_AHEAD = 7
SLOT_MINS = 30

##CACHE
CACHE_FILE = 'calendar_cache.json'
CACHE_TTL_SECONDS = 60 * 60