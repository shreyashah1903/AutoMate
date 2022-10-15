# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import base64
import os.path

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']


def readEmails():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                # your creds file here. Please create json file as here https://cloud.google.com/docs/authentication/getting-started
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:read").execute()
        messages = results.get('messages', [])
        if not messages:
            print('No new messages.')
        else:
            message_count = 0
            for message in messages:
                message_count = message_count + 1
                # TODO Remove this
                if message_count == 200:
                    break

                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    if name == 'From':
                        from_name = values['value']
                        print("From name:" + from_name)
                        if from_name != get_from_address():
                            continue

                        for part in msg['payload']['parts']:
                            try:
                                data = part['body']["data"]
                                byte_code = base64.urlsafe_b64decode(data)

                                text = byte_code.decode("utf-8")
                                text = format_text(text)
                                print("This is the message: " + text)

                                # mark the message as read (optional)
                                msg = service.users().messages().modify(userId='me', id=message['id'],
                                                                        body={'removeLabelIds': ['UNREAD']}).execute()
                            except BaseException as error:
                                pass
    except Exception as error:
        print(f'An error occurred: {error}')


def get_from_address():
    return "HackHarvard <team@hackharvard.io>"


def format_text(text):
    text = remove_html_tags(text)
    return remove_extra_spaces(text)


def remove_html_tags(text):
    cleantext = BeautifulSoup(text)
    return cleantext.text


def remove_extra_spaces(text):
    text = " ".join(text.split())
    print(text)
    return text


if __name__ == '__main__':
    readEmails()
