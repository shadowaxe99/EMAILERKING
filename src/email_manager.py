import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


class EmailManager:
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
                    scopes=['https://www.googleapis.com/auth/gmail.readonly'])
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)
        return service

    def check_for_new_emails(self):
        results = self.service.users().messages().list(userId='me', q='is:unread from:(-me)').execute()
        messages = results.get('messages', [])
        new_emails = []
        if messages:
            for message in messages:
                email = self.service.users().messages().get(userId='me', id=message['id'], format='full').execute()
                new_emails.append(email)
        return new_emails

    def get_attachments(self, email):
        attachments = []
        if 'parts' in email['payload']:
            for part in email['payload']['parts']:
                if 'filename' in part:
                    attachment = self.service.users().messages().attachments().get(
                        userId='me', messageId=email['id'], id=part['body']['attachmentId']).execute()
                    attachments.append(attachment)
        return attachments
