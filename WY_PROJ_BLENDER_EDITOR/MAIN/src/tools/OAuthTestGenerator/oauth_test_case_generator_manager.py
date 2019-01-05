from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import sys
import re # Get string in between 2 strings

filename = "oauth_test_case_generator_util.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "oauth_test_case_generator_generator.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "oauth_test_case_generator_executor.py"
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
OAUTH_TEST_CASE_GENERATOR_TITLE = ""

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
    '''
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    
    # Command line argument options:
    parser.add_argument('-title','--test_case_generator_title', help='Title of current test case generator process.')
    parser.add_argument('-app','--application_name', help='OAuth 2.0 client ID name.')
    parser.add_argument('-ssurl','--google_spreadsheet_url', help='Google Spreadsheet URL.')
    parser.add_argument('-feed','--feed_name', help='Name of the spreadsheet for processing.')
    parser.add_argument('-feedr','--feed_range', help='Range of the spreadsheet for processing.')
    # Parse the command line arguments.
    flags = parser.parse_args(sys.argv[1:])

    #===========================================================================
    # '-title','--test_case_generator_title', help='Title of current 
    # test case generator process.'
    #===========================================================================
    OAUTH_TEST_CASE_GENERATOR_TITLE = flags.test_case_generator_title
    #===========================================================================
    # '-app','--application_name', help='OAuth 2.0 client ID name'
    #===========================================================================
    OAUTH_APPLICATION_NAME = flags.application_name
    #===========================================================================
    # '-ssurl','--google_spreadsheet_url', help='Google Spreadsheet URL'
    #===========================================================================
    GOOGLE_SPREADSHEET_URL = flags.google_spreadsheet_url
    #===========================================================================
    # '-feed','--feed_name', help='Name of the spreadsheet for processing'
    #===========================================================================
    FEED_NAME = str(flags.feed_name) + '!'
    #===========================================================================
    # '-feedr','--feed_range', help='Range of the spreadsheet for processing'
    #===========================================================================
    # If range is not specified then use default "A:Z" range
    if FEED_RANGE == "":
       FEED_RANGE = 'A:Z'

    #===========================================================================
    # Keep the prompted command to generate the makefile for each unit test 
    # case generation
    #===========================================================================
    final_oauth_test_case_generator_command = ""
    current_working_directory = os.getcwd()
    oauth_test_case_cd_dir_command = "cd " + current_working_directory
    oauth_test_case_generator_command = "python oauth_test_case_generator_manager.py -app "  + str(flags.application_name) + " -ssurl " + str(flags.google_spreadsheet_url) + " -feed " + str(flags.feed_name) + "\n"
    final_oauth_test_case_generator_command = oauth_test_case_cd_dir_command + " & " + oauth_test_case_generator_command

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("OAuth test case generator title  : ", OAUTH_TEST_CASE_GENERATOR_TITLE)
    print("Google Spreadssheet URL          : ", GOOGLE_SPREADSHEET_URL)
    print("Google Spreadhsheet feed name    : ", FEED_NAME)
    print("OAUth client application name    : ", OAUTH_APPLICATION_NAME)
    print("OAUth client secret file         : ", OAUTH_CLIENT_SECRET_FILE)

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
    This is the main function for Python unit test case generating tool, also
    the main manager to manage the sub processing functions, 
    where command line arugments are parsed with Python Argparse, and pass the 
    command line arguemnts data into sub functions to generate the unit test
    case according to the data values and informations indicated in the 
    Google Spreadsheet.

    The main framework:
        0. Implement test case data Google Spreadsheet --> 
           Project directory --> Adjust makefile providing spreadsheet URLs 
           --> $ make
        1. Parse command line arguments get 
            - OAuth client application name.
            - OAuth client secret JSON file path.
            - Google Spreadsheet URL.
            - Google Spreadhseet feed name.
            - Google Spreadhseet feed range.
        2. Authenticate with Google using OAuth to access private Google 
           Spreadsheets data.
        3. Get Google Spreadsheet data and process it into Python data 
           structure list. 
           (Also get rid of empty lists inside the lists)
        4. Process spreadsheet data list into unit test case file string 
           and generate the unit test case file onto class's test cases folder.
        6. Execute the generated unit test case file and store the result 
           output onto a text file path also given in the Google Spreadsheet.
           Also generates the HTML Pydoc API documentation for each classes and
           the unit test case files just generated.

    Example:
        The main testing class file name is "WYCoordsys.py" 
	    which is in "WYCoordsys" folder
	    The unit test case related files will be generated under "WYCoordsys/WYCoordsysTestCases" folder
		- Unit test case data file will be named "WYCoordsysTestCaseData_testingfuncname.txt"
		- Unit test case file will be named "WYCoordsysTestCase_testingfuncname.py"
		- Unit test case Pydoc document HTML file will be named "WYCoordsysTestCase_testingfuncname.html"
		- Unit test case execution result output log file will be named "WYCoordsysTestCaseResult_testingfuncname.txt"

	    Example:
		drwxr-xr-x 1 Nickj 197121       0 Oct  4 22:14 WYCoordsys/
			-rw-r--r-- 1 Nickj 197121 63944 Oct  4 22:14 WYCoordsys.py
			drwxr-xr-x 1 Nickj 197121     0 Oct  4 22:18 WYCoordsysTestCases/
				-rw-r--r-- 1 Nickj 197121  29902 Oct  4 22:24 WYCoordsysTestCaseData___init__.txt
				-rw-r--r-- 1 Nickj 197121    152 Oct  4 22:24 WYCoordsysTestCaseResult___init__.txt
				-rw-r--r-- 1 Nickj 197121 344325 Oct  4 22:24 WYCoordsysTestCases___init__.html
				-rw-r--r-- 1 Nickj 197121 192903 Oct  4 22:24 WYCoordsysTestCases___init__.py
		drwxr-xr-x 1 Nickj 197121       0 Oct  3 01:24 WYMain/
		drwxr-xr-x 1 Nickj 197121       0 Sep 26 09:22 WYMaterial/
		drwxr-xr-x 1 Nickj 197121       0 Sep 26 10:46 WYMesh/
		drwxr-xr-x 1 Nickj 197121       0 Sep 26 09:22 WYModel/
		drwxr-xr-x 1 Nickj 197121       0 Sep 26 09:24 WYModelManager/
		drwxr-xr-x 1 Nickj 197121       0 Sep 26 09:23 WYUtil/

    This function calls following sub functions:
        oauth_test_case_generator_generator::oauth_test_case_generator_generator()
            - This function is to generate the unit test case file
              using the information provided within command line arguments.
        oauth_test_case_generator_executor::oauth_test_case_generator_executor()
            - This function is to handle the execution of the external process 
              commands like generating Pydoc HTML page for the unit test cases
              and storing result of the unit test cases execution output into 
              a text file when the output string is returned from this sub 
              function.
    '''
    #===========================================================================
    # Generate test case file
    #===========================================================================
    # Returned final generated test case file absolute path to check if it is 
    # generated properly before executing them
    # Plus, the unit test case execution result output file absolute path
    # combined into a list
    final_path_list = oauth_test_case_generator_generator(GOOGLE_SPREADSHEET_URL, SCOPES,
                                OAUTH_APPLICATION_NAME, OAUTH_CLIENT_SECRET_FILE,
                                FEED_NAME, FEED_RANGE)

    # Index 0 - Unit test case file destination for executing
    final_generated_test_case_file_abs_path = final_path_list[0]
    # Index 1 - Text file path to store the unit test case execution result 
    #           output.
    final_unittestcase_exe_result_file_abs_path = final_path_list[1]

    sub_run_test_batch_file_path = os.path.dirname(os.path.realpath(final_generated_test_case_file_abs_path)) + "/run_test.bat"
    with safe_open_w(sub_run_test_batch_file_path) as text_file:
        text_file.write("python " + final_generated_test_case_file_abs_path + "\n")
        text_file.write("pause\n")
        
    #===========================================================================
    # Execute test case file
    #===========================================================================
    final_unittestcase_exe_result = ""
    # Overwrite the unit test case result output text file if exists
    if os.path.isfile(final_generated_test_case_file_abs_path) == False:
        final_unittestcase_exe_result = oauth_test_case_generator_executor(final_generated_test_case_file_abs_path, final_oauth_test_case_generator_command)
        with open(final_unittestcase_exe_result_file_abs_path, "w") as text_file:
            text_file.write(final_unittestcase_exe_result)
            print("Unit test case result printed                :\n" + final_unittestcase_exe_result + "\n")
        
    # Recreate the unit test case result output text file if not exists
    # Create the directory if the path does not exist using the utility function
    # safe_open_w()
    else:
        final_unittestcase_exe_result = oauth_test_case_generator_executor(final_generated_test_case_file_abs_path, final_oauth_test_case_generator_command)
        with safe_open_w(final_unittestcase_exe_result_file_abs_path) as text_file:
            text_file.write(final_unittestcase_exe_result)
            print("Unit test case result printed                :\n" + final_unittestcase_exe_result + "\n")

    

        





   
