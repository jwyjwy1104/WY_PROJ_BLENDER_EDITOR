import sys
import subprocess

filename = "oauth_time_report_dashboard_util.py"
exec(compile(open(filename).read(), filename, 'exec'))


def oauth_time_report_dashboard_executor(time_report_dashboard_html_file_abs_path):
    '''
    OAuth test case generator executor

    This script is to generate the Pydoc HTML document page of the unit test 
    case is generated through this OAuth test case generator algorithm
    and then execute the unit test case to get the result of the tests and 
    write the result into a log file to keep the in local folder.

    :param test_case_file_abs_path                : 
        Absolute file path of the final unit test case file to execute with.
    :param final_oauth_test_case_generator_command: 
        Final OAuth test case generator execute command to be stored into each
        unit test case folders' makefile, so i can execute them independently.
    '''
    
    #===========================================================================
    # Generate HTML page for current time report dashboard operators:
    #===========================================================================
    current_working_directory = os.getcwd()
    generate_pydoc_html_command = "cd " + current_working_directory + "/Documents & \
                     python -m pydoc -w oauth_time_report_dashboard_generator & \
                     python -m pydoc -w oauth_time_report_dashboard_get_spreadsheet_data & \
                     python -m pydoc -w oauth_time_report_dashboard_executor & \
                     python -m pydoc -w oauth_time_report_dashboard_util"
    stdoutdata = subprocess.getoutput(generate_pydoc_html_command)

    # Return the result output string
    return str(stdoutdata)

