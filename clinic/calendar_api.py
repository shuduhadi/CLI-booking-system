import datetime
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from clinic.config import SCOPES, TOKEN_FILE, CREDENTIALS_FILE, DAYS_AHEAD


def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds

def get_calendar_service():
    creds = get_credentials()
    return build("calendar", "v3", credentials=creds)

def fetch_next_7_days(calendar_id='primary'):
    service = get_calendar_service()
    now = datetime.datetime.now(
        tz=datetime.timezone.utc
    )

    end = now + datetime.timedelta(days=DAYS_AHEAD)
    try:
        events_results = (
            service.events()
            .list(
                calendarId=calendar_id,
                timeMin= now.isoformat(),
                timeMax= end.isoformat(),
                singleEvents= True,
                orderBy="startTime",
            )
            .execute()
        )
        return events_results.get('items', [])
    
    except HttpError as error:
        print('Google Calendar error:', error)
        return []
    
def main():
    events = fetch_next_7_days()
    if not events:
        print('No events found.')
        return
    
    for event in events:
        start = event['start'].get(
            'dateTime', event["start"].get('date')
        )
        summary = event.get('summary', 'No title')
        print(start, '-', summary)

if __name__ == "__main__":
    main()