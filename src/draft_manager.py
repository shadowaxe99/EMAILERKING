import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


class DraftManager:
    def __init__(self):
        self.service = self.create_service()

    def create_service(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                creds = service_account.Credentials.from_service_account_file(
                    os.getenv('GOOGLE_AUTH_CREDENTIALS'),
                    scopes=['https://www.googleapis.com/auth/gmail.compose'])
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)
        return service

    def create_draft(self, message):
        draft = {
            'message': {
                'raw': message
            }
        }
        self.service.users().drafts().create(userId='me', body=draft).execute()

    def get_drafts_to_send(self):
        drafts = self.service.users().drafts().list(userId='me').execute()
        drafts_to_send = []
        if 'drafts' in drafts:
            for draft in drafts['drafts']:
                draft_data = self.service.users().drafts().get(userId='me', id=draft['id']).execute()
                drafts_to_send.append(draft_data)
        return drafts_to_send
