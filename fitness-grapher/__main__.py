import httplib2

import click
from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

# client_id = ''
# client_secret = ''

# scope = 'https://www.googleapis.com/auth/gmail.readonly'

# flow = OAuth2WebServerFlow(client_id, client_secret, scope)

# storage = Storage('credentials.dat')
# credentials = storage.get()

# if credentials is None or credentials.invalid:
#     credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

# http = httplib2.Http()
# http = credentials.authorize(http)

# service = build('gmail', 'v1', http=http)

# try:
#     response = service.users().labels().list(userId='me').execute()
#     print(response)
# except Exception as err:
#     print(err)


@click.command()
@click.argument('client_id')
@click.argument('client_secret')
def main(client_id, client_secret):
    print(client_id)
    print(client_secret)


if __name__ == '__main__':
    main()
