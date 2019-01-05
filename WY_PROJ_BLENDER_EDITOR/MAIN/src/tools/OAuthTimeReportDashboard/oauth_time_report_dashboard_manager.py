from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import sys
import re # Get string in between 2 strings

filename = "oauth_time_report_dashboard_util.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "oauth_time_report_dashboard_generator.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "oauth_time_report_dashboard_executor.py"
exec(compile(open(filename).read(), filename, 'exec'))

#===============================================================================
# Global variables
#===============================================================================
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
GOOGLE_SPREADSHEET_URL = ""
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
OAUTH_APPLICATION_NAME = 'WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT'
OAUTH_CLIENT_SECRET_FILE = 'client_secret.json'
FEED_NAME = ""
FEED_RANGE = ""
OAUTH_TIME_REPORT_DASHBOARD_TITLE = ""
TIME_REPORT_DASHBOARD_HTML_FILE_PATH = ""
#===============================================================================
# Command line argument parser with Python "Argparse"
# Code brought from: https://developers.google.com/sheets/api/quickstart/python 
#===============================================================================
try:
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Python Argparse.

    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This code is to add my own command line arugment options with flags and 
    parse the command line arguments when proper data values are passed into 
    the script execution call with proper command line argument option flags.
    
    Command line argument flags:
    # '-title'      ,'--test_case_generator_title'              , help='Title of current 
    # '-app'        ,'--application_name'                       , help='OAuth 2.0 client ID name'
    # '-ssurl'      ,'--google_spreadsheet_url'                 , help='Google Spreadsheet URL'
    # '-feed'       ,'--feed_name'                              , help='Name of the spreadsheet for processing'
    # '-feedr'      ,'--feed_range'                             , help='Range of the spreadsheet for processing'
    # '-filepath'   ,'--time_report_dashboard_html_file_path'   , help='Time report dashboard HTML file path to write to.'
    '''
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    
    # Command line argument options:
    parser.add_argument('-title','--time_report_dashboard_title', action='append', default=[], help='Title of current time report dashboard.')
    parser.add_argument('-app','--application_name', help='OAuth 2.0 client ID name.')
    parser.add_argument('-ssurl','--google_spreadsheet_url', action='append', default=[], help='Google Spreadsheet URL.')
    parser.add_argument('-feed','--feed_name', help='Name of the spreadsheet for processing.')
    parser.add_argument('-feedr','--feed_range', help='Range of the spreadsheet for processing.')
    parser.add_argument('-filepath','--time_report_dashboard_html_file_path', action='append', default=[], help='Time report dashboard HTML file path to write to.')
    # Parse the command line arguments.
    flags = parser.parse_args(sys.argv[1:])

    # '-title','--test_case_generator_title', help='Title of current 
    # test case generator process.'
    OAUTH_TIME_REPORT_DASHBOARD_TITLE = flags.time_report_dashboard_title
    # '-app','--application_name', help='OAuth 2.0 client ID name'
    OAUTH_APPLICATION_NAME = flags.application_name
    # '-ssurl','--google_spreadsheet_url', help='Google Spreadsheet URL'
    GOOGLE_SPREADSHEET_URL = flags.google_spreadsheet_url
    # '-feed','--feed_name', help='Name of the spreadsheet for processing'
    FEED_NAME = str(flags.feed_name) + '!'
    # '-feedr','--feed_range', help='Range of the spreadsheet for processing'
    # If range is not specified then use default "A:Z" range
    if FEED_RANGE == "":
       FEED_RANGE = 'A:Z'
    # '-filepath','--time_report_dashboard_html_file_path', 
    #  help='Time report dashboard HTML file path to write to.'
    TIME_REPORT_DASHBOARD_HTML_FILE_PATH = flags.time_report_dashboard_html_file_path

    #===========================================================================
    # Keep the prompted command to generate the makefile for each unit test 
    # case generation
    #===========================================================================
    final_oauth_test_case_generator_command = ""
    current_working_directory = os.getcwd()
    oauth_test_case_cd_dir_command = "cd " + current_working_directory
    oauth_test_case_generator_command = "python oauth_test_case_generator_manager.py -app "  + str(flags.application_name) + " -ssurl " + str(flags.google_spreadsheet_url) + " -feed " + str(flags.feed_name) + "\n"
    final_oauth_test_case_generator_command = oauth_test_case_cd_dir_command + " & " + oauth_test_case_generator_command

    print("\n\n=================================================================================================================")
    print("OAuth time report dashboard title                : ", OAUTH_TIME_REPORT_DASHBOARD_TITLE)
    print("Google Spreadssheet URL                          : ", GOOGLE_SPREADSHEET_URL)
    print("Google Spreadhsheet feed name                    : ", FEED_NAME)
    print("OAUth client application name                    : ", OAUTH_APPLICATION_NAME)
    print("OAUth client secret file                         : ", OAUTH_CLIENT_SECRET_FILE)
    print("Time report dashboard HTML page file path        : ", TIME_REPORT_DASHBOARD_HTML_FILE_PATH)
    print("=================================================================================================================\n\n")

    #print(flags)
except ImportError:
    flags = None

#===============================================================================
#===============================================================================
#===============================================================================
# Main function
#===============================================================================
#===============================================================================
#===============================================================================
if __name__ == '__main__':
    '''
    This is the main function for time report dashboard generating tool, also
    the main manager to manage the sub processing functions, 
    where command line arugments are parsed with Python Argparse, and pass the 
    command line arguemnts data into sub functions to generate the time report
    dashboard HTML page designed with amChart.

    The main framework:
        0. Implement time report Google Spreadsheet --> 
           Project directory --> Adjust makefile providing multiple time report
           spreadsheet URLs and file paths --> $ make
        1. Parse command line arguments get 
            - OAuth client application name.
            - OAuth client secret JSON file path.
            - Google Spreadsheet URL.
            - Google Spreadhseet feed name.
            - Google Spreadhseet feed range.
            - Time report dashboard HTML page file path.
        2. Authenticate with Google using OAuth to access private Google 
           Spreadsheets data.
        3. Get Google Spreadsheet data and process it into Python data 
           structure list. 
           (Also get rid of empty lists inside the lists)
        4. If the file exists then load the lists byte code from the text file
           using pickle library and append the new spreadsheet data.
           (This mechanism is to merge the mutiple time report spreadsheet data 
            into single time report dashboard chart)
        5. Write the newly appended spreadsheet data to the local text file in 
           byte codes using pickle library.
           (If multiple time report dashboards are provided with same export  
            file path, then all the data will automatically merged into one)
        6. Generate time report dashboard HTML page with the provided file path.
        7. Open up the generated time report dasboard HTML page on the web 
           browser with "start" command indicated in the makefile.

    This function calls following sub functions:
        oauth_time_report_dashboard_generator::oauth_time_report_dashboard_generator()
            - This function is to generate the time report dashbaord HTML page 
              using the information provided within command line arguments.
        oauth_time_report_dashboard_executor::oauth_time_report_dashboard_executor()
            - This function is to handle the execution of the external process 
              commands like generating Pydoc HTML page for the tool API.
    '''
    #===========================================================================
    # Generate time report dashboard data using the data retrieved from Google
    # Spreadsheet
    #===========================================================================
    html_file_paths = []
    for i in range(0, len(GOOGLE_SPREADSHEET_URL)):
         html_file_path = oauth_time_report_dashboard_generator(GOOGLE_SPREADSHEET_URL[i], SCOPES,
                                OAUTH_APPLICATION_NAME, OAUTH_CLIENT_SECRET_FILE,
                                FEED_NAME, FEED_RANGE, TIME_REPORT_DASHBOARD_HTML_FILE_PATH[i])
         html_file_paths.append(html_file_path)


    #executor_results = []
    #for i in range(0, len(html_file_paths)):
    #    executor_result = oauth_time_report_dashboard_executor(html_file_paths[i])
    #    executor_results.append(executor_result)


    




        





   
