import sys
import subprocess
import re

filename = "oauth_test_case_generator_util.py"
exec(compile(open(filename).read(), filename, 'exec'))

def oauth_test_case_generator_executor(test_case_file_abs_path, 
                                       final_oauth_test_case_generator_command):
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    OAuth test case generator executor

    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This script is to generate the Pydoc HTML document page of the unit test 
    case is generated through this OAuth test case generator algorithm
    and then execute the unit test case to get the result of the tests and 
    write the result into a log file to keep the in local folder.

    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param test_case_file_abs_path: Absolute file path of the final unit test case file to execute with.
    :type  test_case_file_abs_path: string
    :param final_oauth_test_case_generator_command: Final OAuth test case generator execute command to be stored into each unit test case folders' makefile, so i can execute them independently.
    :type  final_oauth_test_case_generator_command: string

    :return stdoutdata: The result of the external processes to be stored inside the local text file.
    :rtype  stdoutdata: string
    '''
    # Generate unit test cases file Pydoc HTML page
    # In order to generate the HTML page in the same directory as the unit test 
    # cases i needed to retrieved the directory path of the unit test case file 
    # and change directory before generating HTML Pydoc page
    unit_test_case_pydoc_html_export_dir_path = os.path.dirname(os.path.realpath(test_case_file_abs_path))
    
    # Get the file name to generate the makefile name
    makefile_name = str(test_case_file_abs_path[len(os.path.dirname(test_case_file_abs_path))+1:]).replace(".py","")

    #===========================================================================
    # Generate HTML page for unit test case file Pydoc:
    #===========================================================================
    generate_pydoc_html_command = "cd " + unit_test_case_pydoc_html_export_dir_path + " & python -m pydoc -w " + test_case_file_abs_path
    print("Unit test case Pydoc HTML file generated     :" + test_case_file_abs_path)
    stdoutdata = subprocess.getoutput(generate_pydoc_html_command)
    #print("oauth_test_case_generator_executor Pydoc generate: |" + str(stdoutdata) + "|")
    ##print("cd " + unit_test_case_pydoc_html_export_dir_path + " & python -m pydoc -w "+ test_case_file_abs_path + " output: |" + str(stdoutdata) + "|")

    #===========================================================================
    # Get unit test case result output:
    #===========================================================================
    execute_unit_test_case_command = "python " + test_case_file_abs_path
    # Get the result output of the unit test case execution
    print("Unit test case executed                      :" + test_case_file_abs_path)
    stdoutdata = subprocess.getoutput(execute_unit_test_case_command)
    stdoutdata = re.sub(r'\n+', '\n\n', stdoutdata).strip()

    #===========================================================================
    # Write failed task into Failed.txt
    #===========================================================================
    test_failed = False
    failed_result_file_path = \
        os.getcwd() + "\\OAuthTestGenerator_Failed.txt"
    succeeded_result_file_path = \
        os.getcwd() + "\\OAuthTestGenerator_Succeeded.txt"
    
    with open(failed_result_file_path, "a") as text_file:
        if stdoutdata.find("FAILED (failures=") != -1:
            test_failed = True
            subprocess.getoutput("mshta \"javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Failed in " + test_case_file_abs_path.replace("\\", "\\\\") + "!',0, 'Setup Error!', 64 );close()\"")
            text_file.write("FAILED: " + test_case_file_abs_path.replace("\\", "\\\\") + "\n")
        if stdoutdata.find("SyntaxError") != -1:
            test_failed = True
            subprocess.getoutput("mshta \"javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'SyntaxError in " + test_case_file_abs_path.replace("\\", "\\\\") + "!',0, 'Setup Error!', 64 );close()\"")
            text_file.write("SyntaxError: " + test_case_file_abs_path.replace("\\", "\\\\") + "\n")
        if stdoutdata.find("ERROR: test") != -1:
            test_failed = True
            subprocess.getoutput("mshta \"javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Error in " + test_case_file_abs_path.replace("\\", "\\\\") + "!',0, 'Setup Error!', 64 );close()\"")
            text_file.write("ERROR: " + test_case_file_abs_path.replace("\\", "\\\\") + "\n")

    #===========================================================================
    # Write succeeded task into Succeeded.txt
    #===========================================================================
    with open(succeeded_result_file_path, "a") as text_file:
        if test_failed == False:
            text_file.write("Succeeded: " + test_case_file_abs_path.replace("\\", "\\\\") + "\n")


    #===========================================================================
    # Create sub makefile in each test case folder:
    #===========================================================================
    # Current makefile path
    sub_makefile_path = unit_test_case_pydoc_html_export_dir_path + \
                        "\\makefile_" + makefile_name
    sub_makefile_str = ""
    # Makefile start
    sub_makefile_str += "all:\n"
    # Execute oauth test case generator command
    sub_makefile_str += "\t" + final_oauth_test_case_generator_command + "\n"
    # Generate Pydoc HTML command
    sub_makefile_str += "\t" + generate_pydoc_html_command + "\n"
    # Execute unit test cases command
    sub_makefile_str += "\t" + execute_unit_test_case_command + "\n"

    sub_makefile_str = sub_makefile_str.replace("\\", "\\\\")
    with safe_open_w(sub_makefile_path) as text_file:
        text_file.write(sub_makefile_str)

    # Batch file to run make
    run_makefile_batch_path = unit_test_case_pydoc_html_export_dir_path + \
                              "\\run_makefile.bat"
    with safe_open_w(run_makefile_batch_path) as text_file:
        text_file.write("make -f " + sub_makefile_path)
    #===========================================================================

    # Return the unit test case execution result output string
    return str(stdoutdata)

