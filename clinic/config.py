"""
Central configuration for the clinic booking system.
"""
## Google Calendar
STUDENT_CALENDAR_ID = 'primary'

CLINIC_CALENDAR_ID = (
    "bec7fee45ddb51ae1553c1837129802fcfe10198035691130a9808979924f494"
    "@group.calendar.google.com"
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