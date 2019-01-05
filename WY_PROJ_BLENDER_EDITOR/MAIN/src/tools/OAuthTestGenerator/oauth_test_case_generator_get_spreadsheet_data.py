from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import sys

#===============================================================================
#===============================================================================
#===============================================================================
# Get valid OAuth credential function
# Code brought from: https://developers.google.com/sheets/api/quickstart/python 
#===============================================================================
#===============================================================================
#===============================================================================
def get_credentials(scopes, oauth_client_application_name, oauth_client_secret_json_file):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Gets valid user credentials from storage.

    Called by function: oauth_test_case_generator_get_spreadsheet_data::oauth_test_case_generator_get_spreadsheet_data()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function authenticates OAuth client with Google to get the access
    to the private Google Spreadsheets.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    ------------------------------------------------------------------------
    Resources:
    ------------------------------------------------------------------------
    Code brought from: https://developers.google.com/sheets/api/quickstart/python
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param scopes: Modifying scopes.
    :type  scopes: string
        Example: scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    :param oauth_client_application_name: OAuth client application name.
    :type  oauth_client_application_name: string
    :param oauth_client_secret_json_file: OAuth client secret JSON file path.
    :type  oauth_client_secret_json_file: string

    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return credentials: Credentials, the obtained credential.
    :rtype  credentials: Credentials
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-client_secret.json')

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/sheets.googleapis.com-python-quickstart.json
    # scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(oauth_client_secret_json_file, scopes)
        flow.user_agent = oauth_client_application_name
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    # Return the obtained credential.
    return credentials

#===============================================================================
#===============================================================================
#===============================================================================
# Sub main function
# Code brought from: https://developers.google.com/sheets/api/quickstart/python 
#===============================================================================
#===============================================================================
#===============================================================================
def oauth_test_case_generator_get_spreadsheet_data(google_spreadsheet_url, scopes,
                                oauth_client_application_name, oauth_client_secret_json_file,
                                feed_name, feed_range):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Gets valid user credentials from storage.

    Called by function: oauth_test_case_generator_generator::oauth_test_case_generator_generator()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function authenticates OAuth client with Google to get the access
    to the private Google Spreadsheets and retrieved the data from the Google
    Spreadsheet and organize them into list data structure for further 
    processsing.

    Creates a Sheets API service object and return the list data structure 
    containing all the data values stored in the Google Spreadsheet being 
    accessed.
    ------------------------------------------------------------------------
    Resources:
    ------------------------------------------------------------------------
    Code brought from: https://developers.google.com/sheets/api/quickstart/python
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param google_spreadsheet_url: Googel Spreadsheet URL to retrieve the data from.
    :type  google_spreadsheet_url: string
    :param scopes: Modifying scopes.
    :type  scopes: string
        Example: scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    :param oauth_client_application_name: OAuth client application name.
    :type  oauth_client_application_name: string
    :param oauth_client_secret_json_file: OAuth client secret JSON file path.
    :type  oauth_client_secret_json_file: string
    :param feed_name: Name of the Google Spreadsheet feed to retrieved data from.
    :type  feed_name: string
    :param feed_range: Range of the feed data cells to retrieve with.
    :type  feed_range: string

    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return spreadsheetData: List data structure containg all the data retrieved from provided Google Spreadsheet URL and provided feed name with provided feed range.
    :rtype  spreadsheetData: []
    """

    credentials = get_credentials(scopes, oauth_client_application_name, oauth_client_secret_json_file)
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    #===========================================================================
    # Spreadsheet URL ID in between "/d/" and "/edit"
    #===========================================================================
    #print("SPREADSHEET_URL" + SPREADSHEET_URL)
    # Get spreadsheet ID string inside the URL passed from command line argv
    spreadsheetId = re.search('/d/(.*)/edit', google_spreadsheet_url)
    spreadsheetId = spreadsheetId.group(1)

    # spreadsheetId = '1WReZYyjIMcfau-9TfERLZtquK7Tx1kRhHKCTfv1u184'
    #===========================================================================
    # Range of the data field (eg. Can specify the feed name like "Sheet1!A:F")
    # Feed name can be empty ""
    #===========================================================================
    if feed_range == "":
        rangeName = feed_name + 'A:Z'
    else:
        rangeName = feed_name + feed_range
    
    #===========================================================================
    # Get spreadsheet data
    #===========================================================================
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    spreadsheetData = result.get('values', [])

    #===========================================================================
    # Parse spreadsheet data retrieved
    #===========================================================================
    if not spreadsheetData:
        print('No data found.')
    return spreadsheetData

