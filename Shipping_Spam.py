# Line 42, line 61, line 68 - These are the lines where you have to insert your Label ID. No other changes needed.

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from Email_Formatter import EmFmt

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/gmail.settings.basic','https://www.googleapis.com/auth/gmail.readonly']

def spammer(txt):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    # Everything till here is default code added by google for authentication.

    #Get the existing filter's ID by searching for the Shipping Spam Label's ID & then picking the Filter ID indirectly. Filter ID will keep changing whenever i delete & add a new one, but Filter ID will remain constant until deletion.
    filters = service.users().settings().filters().list(userId='me').execute()
    for f in filters['filter']:
        if f['action'].get('addLabelIds',"") == ['INSERT_YOUR_LABELID_HERE']:
            currFilId =  f['id']
            currEmIds = f['criteria']['from']

    input, inpWtoutOr = EmFmt(txt)

    if input != "":
        newEmIds = currEmIds + " OR " + input
    else:
        newEmIds=currEmIds
        return 'No new emails supplied.'

    #this will apply the label Shipping Spam to the exisiting messages in the inbox & remove them from therein.
    for emailId in inpWtoutOr:
        resource = service.users().threads().list(userId='me', q=emailId).execute()
        threads = []
        for t in resource.get('threads',""):
            if t != "": #in case the email ID supplied doesn't have an existing mail, it will pass.
                threads.append(t['id']) #obtains the ID of matching thread and appends it to the empty list
                payload = {'addLabelIds': ['INSERT_YOUR_LABELID_HERE'],\
                 'removeLabelIds': ['INBOX']}
                for t in threads:
                    service.users().threads().modify(userId='me', id=t, body=payload).execute()

    # create the new filter:
    payload = {'criteria': {'from': newEmIds},'action': \
    {'addLabelIds': ['INSERT_YOUR_LABELID_HERE'],'removeLabelIds': ['INBOX']}}
    service.users().settings().filters().create(userId='me', body=payload).execute()

    # # delete the existing filter
    service.users().settings().filters().delete(userId='me', id=currFilId).execute()
    return (f"These IDs have been added to the filter: {inpWtoutOr}")


if __name__ == '__main__':
    spammer(txt)
