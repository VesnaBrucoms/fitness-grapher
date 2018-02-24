import httplib2
import logging

import click
from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

from . import service_details


SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'


@click.command()
@click.argument('client_id')
@click.argument('client_secret')
@click.option('-l', '--log-level', default='INFO', help='Logging detail level')
def main(client_id, client_secret, log_level):
    logging.basicConfig(level=log_level)
    logging.info('Fitness Grapher v%s\n', service_details['version'])

    logging.info('Authenticating')
    flow = OAuth2WebServerFlow(client_id, client_secret, SCOPE)

    storage = Storage('credentials.dat')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        flags = tools.argparser.parse_args('--auth_host_name localhost '
                                           '--noauth_local_webserver'.split())
        credentials = tools.run_flow(flow, storage, flags)

    http = httplib2.Http()
    http = credentials.authorize(http)
    logging.info('Authentication successful')

    logging.info('Building service')
    service = build('gmail', 'v1', http=http)

    try:
        response = service.users().labels().list(userId='me').execute()

        fitbit_label = None
        for label in response['labels']:
            if label['name'] == 'Fitbit':
                fitbit_label = label
                print(label)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
