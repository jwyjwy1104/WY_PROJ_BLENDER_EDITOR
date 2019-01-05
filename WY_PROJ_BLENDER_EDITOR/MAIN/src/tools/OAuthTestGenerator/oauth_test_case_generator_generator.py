import sys
import os
import re # Get string in between 2 strings

filename = "oauth_test_case_generator_util.py"
exec(compile(open(filename).read(), filename, 'exec'))

filename = "oauth_test_case_generator_get_spreadsheet_data.py"
exec(compile(open(filename).read(), filename, 'exec'))
def sub_process_data_generate_test_case_file_header(test_case_unittestcase_class_header_imports,
                                               test_case_testing_class_file_name, test_case_unittestcase_class_name, test_case_unittestcase_class_description,
                                               test_case_normal_case_counter, test_case_boundary_case_counter, test_case_error_case_counter, 
                                               test_case_white_box_counter, test_case_black_box_counter):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Test cases generator sub function to help generating the unit test case 
    function inner comment Pydoc docstring.

    Called by function  : process_google_spreadsheet_test_case_data()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function generates the unit test case file header to handle the extra
    import codes, main unit test case file class definition and class inner
    comment Pydoc documentation with summarized data values which contains 
    what type of and how many test cases are generated and tested in this unit
    test case file.
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param test_case_unittestcase_class_header_imports: Import code provided in the spreadsheet to be inserted at the very top of the unit test case file.
    :type  test_case_unittestcase_class_header_imports: string
    :param test_case_testing_class_file_name: Name of the testing class Python file to pre-compile to apply the changes before testing.
    :type  test_case_testing_class_file_name: string
    :param test_case_unittestcase_class_name: Unit test case file class name for class definition.
    :type  test_case_unittestcase_class_name: string
    :param test_case_unittestcase_class_description: Unit test case class description.
    :type  test_case_unittestcase_class_description: string
    :param test_case_normal_case_counter: Number of normal test cases inserted to this unit test case file.
    :type  test_case_normal_case_counter: string
    :param test_case_error_case_counter: Number of error test cases inserted to this unit test case file.
    :type  test_case_error_case_counter: string
    :param test_case_boundary_case_counter: Number of boundary test cases inserted to this unit test case file.
    :type  test_case_boundary_case_counter: string
    :param test_case_white_box_counter: Number of white box test cases inserted to this unit test case file.
    :type  test_case_white_box_counter: string
    :param test_case_black_box_counter: Number of black box test cases inserted to this unit test case file.
    :type  test_case_black_box_counter: string
    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return final_test_case_header_str: Return final unit test case file header string which contains import code, class definition, class inner document Pydoc docstring and the summarized testing data informations.
    :rtype  final_test_case_header_str: string
    """
    current_working_directory = os.getcwd()
    final_testing_class_file_name = current_working_directory  + "\\" + test_case_testing_class_file_name
    final_test_case_header_str = ""
    #===========================================================================
    # Unit test case class definition
    #===========================================================================
    # Add extra imports indicated in the Google Spreadsheet
    final_test_case_header_str +=  test_case_unittestcase_class_header_imports + "\n"
    final_test_case_header_str += "import os\n" 
    final_test_case_header_str += "import sys\n" 
    final_test_case_header_str += "import math\n" 
    final_test_case_header_str += "import unittest\n" 
    final_test_case_header_str += "precompile_filename = \"" +  final_testing_class_file_name.replace("\\", "\\\\") + "\"\n"
    final_test_case_header_str += "exec(compile(open(precompile_filename).read(), precompile_filename , 'exec'))\n\n"
    final_test_case_header_str += "class " + test_case_unittestcase_class_name + "(unittest.TestCase):\n"
    final_test_case_header_str += "    \"\"\"" + "\n"
    final_test_case_header_str += "    " + test_case_unittestcase_class_description + "\n\n"
    final_test_case_header_str += "    ----------------------------------------------------------------------\n"
    final_test_case_header_str += "    Summary\n"
    final_test_case_header_str += "    ----------------------------------------------------------------------\n"
    final_test_case_header_str += "        Number of normal case test     :" + str(test_case_normal_case_counter) + "\n"
    final_test_case_header_str += "        Number of boundary case test   :" + str(test_case_boundary_case_counter) + "\n"
    final_test_case_header_str += "        Number of error case test      :" + str(test_case_error_case_counter) + "\n"
    final_test_case_header_str += "        Number of white box test       :" + str(test_case_white_box_counter) + "\n"
    final_test_case_header_str += "        Number of black box test       :" + str(test_case_black_box_counter) + "\n"
    final_test_case_header_str += "    \"\"\"" + "\n"

    # Return final unit test case file header string which contains import code,
    # class definition, class inner document Pydoc docstring and 
    # the summarized testing data informations.
    return final_test_case_header_str


def sub_process_data_generate_test_case_function_pydoc(spreadsheetData, 
                                     test_case_id, test_case_title, test_case_description, 
                                     test_case_class_name, test_case_function_name, test_case_testing_function_return_type, test_case_variable_name, 
                                     test_case_class_obj_allocation_param_arr, test_case_class_obj_allocation_param_arr_counter, test_case_class_obj_allocation_param_starting_index, 
                                     test_case_class_testing_function_input_param_arr, test_case_class_testing_function_input_param_arr_counter, test_case_class_testing_function_input_param_starting_index,
                                     test_case_class_testing_function_expected_result_arr, test_case_class_testing_function_expected_result_arr_counter, test_case_class_testing_function_expected_output_starting_index,
                                     test_case_param_name_cells_row, test_case_param_type_cells_row, test_case_param_description_cells_row):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Test cases generator sub function to help generating the unit test case 
    function inner comment Pydoc docstring.

    Called by function  : sub_process_data_generate_current_test_case_function_str()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function generates each unit test case function inner comments Pydoc 
    docstring to be appended to the unit test case function body to generate 
    the Pydoc HTML page for all the unit test cases after.

    This is where the Pydoc docstring is generated to be appended after the 
    "def" function definition line.
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param spreadsheetData: Spreadsheet data in Python list data structure format.
    :type  spreadsheetData: [[],[],[] ...]
    :param test_case_id: Test case ID. (eg. TC_NC_01, TC_NC_02, TC_EC0_01 ... )
    :type  test_case_id: string
    :param test_case_title: Test case title.
    :type  test_case_title: string
    :param test_case_description: Test case description.
    :type  test_case_description: string
    :param test_case_class_name: Test case class name for unit test case class definition.
    :type  test_case_class_name: string
    :param test_case_function_name: Test case function name for each test cases.
    :type  test_case_function_name: string
    :param test_case_testing_function_return_type: Return type of the testing function.
    :type  test_case_testing_function_return_type: string
    :param test_case_variable_name: Name of the variable to allocate with testing class object to test the testing functions.
    :type  test_case_variable_name: string
    :param test_case_class_obj_allocation_param_arr: List data structure containing all parameter values for testing class object allocation.
    :type  test_case_class_obj_allocation_param_arr: []
    :param test_case_class_obj_allocation_param_arr_counter: Number of the parameters to be passed into the testing class object allocation init call.
    :type  test_case_class_obj_allocation_param_arr_counter: int
    :param test_case_class_obj_allocation_param_starting_index: Allocation parameters starting column index, because there could be many or none depending on the constructors to use to allocate the object.
    :type  test_case_class_obj_allocation_param_starting_index: int
    :param test_case_class_testing_function_input_param_arr: List data structure containing all parameter values of the testing function test case data inputs.
    :type  test_case_class_testing_function_input_param_arr: []
    :param test_case_class_testing_function_input_param_arr_counter: Number of the parameters to be passed into the testing function call.
    :type  test_case_class_testing_function_input_param_arr_counter: int
    :param test_case_class_testing_function_input_param_starting_index: Input parameters starting column index, because there could be many or none depending on the function definition.
    :type  test_case_class_testing_function_input_param_starting_index: int
    :param test_case_class_testing_function_expected_result_arr: List data structure containing all the expected value to compare the testing function return value to test the function.
    :type  test_case_class_testing_function_expected_result_arr: []
    :param test_case_class_testing_function_expected_result_arr_counter: Number of the expected results for testing.
    :type  test_case_class_testing_function_expected_result_arr_counter: int
    :param test_case_class_testing_function_expected_output_starting_index: Expected result starting column index because there could be many expected results to compare with.
    :type  test_case_class_testing_function_expected_output_starting_index: int
    :param test_case_param_name_cells_row: Index of the parameter name cells row.
    :type  test_case_param_name_cells_row: int
    :param test_case_param_type_cells_row: Index of the parameter type cells row
    :type  test_case_param_type_cells_row: int
    :param test_case_param_description_cells_row: Index of the parameter description cells row
    :type  test_case_param_description_cells_row: int
    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return cur_test_case_function_pydoc_str: Return currnt test case function inner comment Pydoc docstring code to be appended to the unit test case function definition.
    :rtype  cur_test_case_function_pydoc_str: string
    """
    #===========================================================================
    # Test case functions Pydoc string
    #===========================================================================
    cur_test_case_function_pydoc_str = ""
    cur_test_case_function_pydoc_str += "        \"\"\"\n"
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        Title:\n"
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        " + test_case_title + "\n\n"
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        Description:\n"
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        " + test_case_description + "\n"

    #===========================================================================
    # @param - Class object allocation __init__ call parameters and parameter types
    #===========================================================================
    # This Pydoc is only needed for __init__ constructor test cases
    if test_case_function_name == "__init__":
        cur_test_case_function_pydoc_str += "        \n"
        cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
        cur_test_case_function_pydoc_str += "        Class object allocation __init__ parameters:\n"
        cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
        for k in range(0, test_case_class_obj_allocation_param_arr_counter):
            # Index of the param column cells starting from 7 but this might change 
            # later on so used a variable instead of number
            cur_param_cell_column = test_case_class_obj_allocation_param_starting_index + k

            # Retrieve parameter name from the parameter name row "test_case_param_name_row"
            cur_param_name = str(spreadsheetData[test_case_param_name_cells_row][cur_param_cell_column]).replace(" ", "")
            # Retrieve parameter type from the parameter type row "test_case_param_type_row"
            cur_param_type = str(spreadsheetData[test_case_param_type_cells_row][cur_param_cell_column]).replace(" ", "")
            # Retrieve parameter description from the parameter description row "test_case_param_description_row"
            cur_param_description = str(spreadsheetData[test_case_param_description_cells_row][cur_param_cell_column]).rstrip()
            # Retrieve current test case input parameter value
            cur_param_test_value = test_case_class_obj_allocation_param_arr[k].replace(" ", "")

            # :param [Parmeter name]: [Parameter description]
            cur_test_case_function_pydoc_str += "        :param " + cur_param_name + ": " + cur_param_description + ".\n"
            # :type  [Parmeter name]: [Parameter type]
            cur_test_case_function_pydoc_str += "        :type  " + cur_param_name + ": " + cur_param_type + ".\n"
        
            # :test [Parameter name]: [Parameter test cases data input value]
            cur_test_case_function_pydoc_str += "        :test  " + cur_param_name + ": " + cur_param_test_value + ".\n\n"
    else:
        #=======================================================================
        # @param - Testing function call parameters and parameter types
        #=======================================================================
        if test_case_class_testing_function_input_param_arr_counter > 0:
            cur_test_case_function_pydoc_str += "        \n"
            cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
            cur_test_case_function_pydoc_str += "        Testing function input parameters:\n"
            cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
        for k in range(0, test_case_class_testing_function_input_param_arr_counter):
            # Actual testing functio input parameters should be right after the 
            # class object allocation parameter columns
            cur_param_cell_column = test_case_class_testing_function_input_param_starting_index + k

            # Retrieve parameter name from the parameter name row "test_case_param_name_row"
            cur_param_name = str(spreadsheetData[test_case_param_name_cells_row][cur_param_cell_column]).replace(" ", "")
            # Retrieve parameter type from the parameter type row "test_case_param_type_row"
            cur_param_type = str(spreadsheetData[test_case_param_type_cells_row][cur_param_cell_column]).replace(" ", "")
            # Retrieve parameter description from the parameter description row "test_case_param_description_row"
            cur_param_description = str(spreadsheetData[test_case_param_description_cells_row][cur_param_cell_column]).rstrip()
            # Retrieve current test case input parameter value
            cur_param_test_value = str(test_case_class_testing_function_input_param_arr[k]).replace(" ", "")

            # :param [Parmeter name]: [Parameter description]
            cur_test_case_function_pydoc_str += "        :param " + cur_param_name + ": " + cur_param_description + ".\n"
            # :type  [Parmeter name]: [Parameter type]
            cur_test_case_function_pydoc_str += "        :type  " + cur_param_name + ": " + cur_param_type + ".\n"
            # :test [Parameter name]: [Parameter test cases data input value]
            cur_test_case_function_pydoc_str += "        :test  " + cur_param_name + ": " + cur_param_test_value + ".\n\n"
       
    #===========================================================================
    # @return - Testing function return values and return types
    #===========================================================================
    # :return:
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        Return:\n"
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        :return: Return initialized " + test_case_class_name + " object with member variables intialized properly\n"
    cur_test_case_function_pydoc_str += "        :rtype : " + test_case_testing_function_return_type + "\n"

    #===========================================================================
    # @expect - Testing function expected output values
    #===========================================================================
    # :expect:
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    cur_test_case_function_pydoc_str += "        Expected result:\n"
    cur_test_case_function_pydoc_str += "        ----------------------------------------------------------------------\n"
    for k in range(0, test_case_class_testing_function_expected_result_arr_counter):
        if test_case_variable_name != "":
            cur_test_case_function_pydoc_str += "        :expect: " + str(test_case_class_testing_function_expected_result_arr[k]).replace("\\", "\\\\") + "\n"
        else:
            cur_test_case_function_pydoc_str += "        :expect: " + str(test_case_class_testing_function_expected_result_arr[k]).replace("\\", "\\\\") + "\n"
    cur_test_case_function_pydoc_str += "        \"\"\""

    # Return current test case function Pydoc docstring
    return cur_test_case_function_pydoc_str

def sub_process_data_generate_test_case_function(spreadsheetData, 
                                     cur_test_case_function_pydoc_str,
                                     test_case_id, test_case_title, test_case_description, 
                                     test_case_class_name, test_case_function_name, test_case_testing_function_return_type, test_case_variable_name, 
                                     test_case_class_obj_allocation_param_arr, test_case_class_obj_allocation_param_arr_counter, test_case_class_obj_allocation_param_starting_index, 
                                     test_case_class_testing_function_input_param_arr, test_case_class_testing_function_input_param_arr_counter, test_case_class_testing_function_input_param_starting_index,
                                     test_case_class_testing_function_expected_result_arr, test_case_class_testing_function_expected_result_arr_counter, test_case_class_testing_function_expected_output_starting_index,
                                     code_lines_before_function_body_str, code_lines_after_function_body_str,
                                     test_case_param_name_cells_row, test_case_param_type_cells_row, test_case_param_description_cells_row,
                                     test_case_function_body_full_code_exist, test_case_function_body_full_code_str):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Test cases generator sub function to help generating the unit test case 
    function definition and body implementation code.

    Called by function  : sub_process_data_generate_current_test_case_function_str()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function generates each unit test case function definition 
    and the function body implementation code string for each using the data 
    indicated on each spreadsheet row and return the code string of the unit 
    test case function definition combined with the Pydoc inner comments 
    provided final

    This is where the function definition "def" code is generated and append 
    the pre-generated function Pydoc inner comments passed in as one of the 
    paramters called "cur_test_case_function_pydoc_str", to combine them into 
    final unit test case function string.

    If the testing function body full code implementation exist in the Google 
    Spreadsheet test case data, then use the data value to generate the test 
    case function and return, and other parameter and expected result values 
    will be used for Pydoc generation only so the test case function body will 
    implemented with the "Test case funciton body full code" column cell value
    only.

    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param spreadsheetData: Spreadsheet data in Python list data structure format.
    :type  spreadsheetData: [[],[],[] ...]
    :param cur_test_case_function_pydoc_str: Pydoc inner comment code string to be appended after the function definition line.
    :type  cur_test_case_function_pydoc_str: string
    :param test_case_id: Test case ID. (eg. TC_NC_01, TC_NC_02, TC_EC0_01 ... )
    :type  test_case_id: string
    :param test_case_title: Test case title.
    :type  test_case_title: string
    :param test_case_description: Test case description.
    :type  test_case_description: string
    :param test_case_class_name: Test case class name for unit test case class definition.
    :type  test_case_class_name: string
    :param test_case_function_name: Test case function name for each test cases.
    :type  test_case_function_name: string
    :param test_case_testing_function_return_type: Return type of the testing function.
    :type  test_case_testing_function_return_type: string
    :param test_case_variable_name: Name of the variable to allocate with testing class object to test the testing functions.
    :type  test_case_variable_name: string
    :param test_case_class_obj_allocation_param_arr: List data structure containing all parameter values for testing class object allocation.
    :type  test_case_class_obj_allocation_param_arr: []
    :param test_case_class_obj_allocation_param_arr_counter: Number of the parameters to be passed into the testing class object allocation init call.
    :type  test_case_class_obj_allocation_param_arr_counter: int
    :param test_case_class_obj_allocation_param_starting_index: Allocation parameters starting column index, because there could be many or none depending on the constructors to use to allocate the object.
    :type  test_case_class_obj_allocation_param_starting_index: int
    :param test_case_class_testing_function_input_param_arr: List data structure containing all parameter values of the testing function test case data inputs.
    :type  test_case_class_testing_function_input_param_arr: []
    :param test_case_class_testing_function_input_param_arr_counter: Number of the parameters to be passed into the testing function call.
    :type  test_case_class_testing_function_input_param_arr_counter: int
    :param test_case_class_testing_function_input_param_starting_index: Input parameters starting column index, because there could be many or none depending on the function definition.
    :type  test_case_class_testing_function_input_param_starting_index: int
    :param test_case_class_testing_function_expected_result_arr: List data structure containing all the expected value to compare the testing function return value to test the function.
    :type  test_case_class_testing_function_expected_result_arr: []
    :param test_case_class_testing_function_expected_result_arr_counter: Number of the expected results for testing.
    :type  test_case_class_testing_function_expected_result_arr_counter: int
    :param test_case_class_testing_function_expected_output_starting_index: Expected result starting column index because there could be many expected results to compare with.
    :type  test_case_class_testing_function_expected_output_starting_index: int
    :param code_lines_before_function_body_str: The lines of codes to be prepended to the test case function body codes.
    :type  code_lines_before_function_body_str: string
    :param code_lines_after_function_body_str: The lines of codes to be appended to the test case function body codes.
    :type  code_lines_after_function_body_str: string

    :param test_case_param_name_cells_row: Index of the parameter name cells row.
    :type  test_case_param_name_cells_row: int
    :param test_case_param_type_cells_row: Index of the parameter type cells row
    :type  test_case_param_type_cells_row: int
    :param test_case_param_description_cells_row: Index of the parameter description cells row
    :type  test_case_param_description_cells_row: int

    :param test_case_function_body_full_code_exist: Boolean flag to check whether the testing function full body implementation code exists to decide on how to implement the test cases
    :type  test_case_function_body_full_code_exist: boolean
    :param test_case_function_body_full_code_str: The string of the testing function full body implementation code to be inserted to the test case if exist.
    :type  test_case_function_body_full_code_str: string
    
    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return cur_test_case_function_str: Return currnt test case function string where Pydoc is appended and the function body is implemented
    :rtype  cur_test_case_function_str: string
    """
    # Reset current function string
    cur_test_case_function_str = ""

    #===========================================================================
    # Function definition
    #===========================================================================
    cur_test_case_function_str += "    def test_" + test_case_class_name + "TestCase_" + test_case_function_name + "_" + test_case_id + "(self):\n"
    #===========================================================================
    # Add current test case function pydoc string after the functiond definition
    #===========================================================================
    # Get current test case function Pydoc docstring
    cur_test_case_function_str += cur_test_case_function_pydoc_str + "\n"
    #===========================================================================

    #===========================================================================
    #===========================================================================
    # If the full body implementation code exists, then generate the test case 
    # function with the full body code provided in the spreadsheet
    #===========================================================================
    #===========================================================================
    if test_case_function_body_full_code_exist == True:
        cur_test_case_function_str += test_case_function_body_full_code_str + "\n"
    #===========================================================================
    #===========================================================================
    # If no full body implementation code exists, then generate the test case
    # function using the data values provided in other column cells
    #===========================================================================
    #===========================================================================
    else:
        #===========================================================================
        # Prepend the codes lines before the function body codes using the string 
        # indicated in the spreadsheet
        #===========================================================================
        cur_test_case_function_str += code_lines_before_function_body_str + "\n"
        #===========================================================================

        #===========================================================================
        # Allocating objects with __init__ call with allocation parameters array
        #===========================================================================
        cur_test_case_function_str += "        " + test_case_variable_name + " = " + test_case_class_name + "("
        # Concat all the input parameter string
        for k in range(0, test_case_class_obj_allocation_param_arr_counter):
            if k > 0 and k < test_case_class_obj_allocation_param_arr_counter:
                cur_test_case_function_str += ","
            cur_test_case_function_str += str(test_case_class_obj_allocation_param_arr[k]).replace(" ", "")
        cur_test_case_function_str += ")\n"

        

        #===========================================================================
        # Concat all assertion with expected outputs
        #===========================================================================
        if test_case_function_name == "__init__":
            # Testing __init__ function is a little bit different.
            for k in range(0, test_case_class_testing_function_expected_result_arr_counter):
                cur_test_case_function_str += "        self.assertTrue(" + test_case_variable_name + "." + test_case_class_testing_function_expected_result_arr[k] + ")\n"
        elif test_case_function_name == "__str__":
            # Testing __init__ function is a little bit different.
            for k in range(0, test_case_class_testing_function_expected_result_arr_counter):
                cur_test_case_function_str += "        self.assertTrue(str(" + test_case_variable_name + ") == " + test_case_class_testing_function_expected_result_arr[k] + ")\n"
        # Normal member function testing:
        #   If input parameters are not empty then append the parameter values
        #   to the testing memeber function call.
        #   eg. member_function(a,b,c)
        #   If input parameters are empty then just call the member function.
        #   eg. member_function()
        else:
            #===========================================================================
            # Calling testing function with input parameters array
            #===========================================================================
            # If current test case testing class function parameter array counter is not
            # 0, then it means i am testing a member function inside a class, so i need 
            # to add the member function calling code in the test case to test them
            if test_case_class_testing_function_input_param_arr_counter > 0:
                cur_test_case_function_str += "        testresult = " + test_case_variable_name + "." + test_case_function_name + "("
                for k in range(0, test_case_class_testing_function_input_param_arr_counter):
                    if k > 0 and k < test_case_class_testing_function_input_param_arr_counter:
                        cur_test_case_function_str += ","
                    cur_test_case_function_str += str(test_case_class_testing_function_input_param_arr[k]).replace(" ", "")
                cur_test_case_function_str += ")\n"
            else:
                cur_test_case_function_str += "        testresult = " + test_case_variable_name + "." + test_case_function_name + "()"

            # Testing all other functions
            for k in range(0, test_case_class_testing_function_expected_result_arr_counter):
                cur_test_case_function_str += "        self.assertTrue(testresult == " + test_case_class_testing_function_expected_result_arr[k] + ")\n"

        #===========================================================================
        # Append the codes lines after the function body codes using the string 
        # indicated in the spreadsheet
        #===========================================================================
        cur_test_case_function_str += code_lines_after_function_body_str + "\n"
        #===========================================================================

    # Return currnt test case function string where Pydoc is appended 
    # and the function body is implemented
    return cur_test_case_function_str


def sub_process_data_generate_current_test_case_function_str(spreadsheetData, rowIndex, test_case_title_cells_row, 
                                            test_case_param_name_cells_row, test_case_param_type_cells_row, test_case_param_description_cells_row):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Test cases generator sub function to help generating the unit test case 
    function of each unit test case file which contains Pydoc inner comments
    and test case function code.

    Called by function  : process_google_spreadsheet_test_case_data()
    Calling sub function: sub_process_data_generate_test_case_function()
    Calling sub function: sub_process_data_generate_test_case_function_pydoc()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function generates each unit test case function string for each 
    spreadsheet row data where test case function information is indicated in 
    each spreadsheet row.

    Sub function: sub_process_data_generate_test_case_function()
                  Return the test case function definition and implemented 
                  test case function body code string.
    Sub function: sub_process_data_generate_test_case_function_pydoc()
                  Return the test case function Pydoc inner document string.

    This function calls sub functions to generate the Pydoc inner comments of 
    current test case function 
    Then pass the Pydoc inner comment code to another sub function to 
    genreate the test case function code string to generate the final unit test 
    case function for each spreadsheet row data test cases.

    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :param spreadsheetData: Spreadsheet data in Python list data structure format.
    :type  spreadsheetData: [[],[],[] ...]
    :param rowIndex: Index of the current processing spreadsheet data row.
    :type  rowIndex: int
    :param test_case_title_cells_row: Row number of the title cells to get the column index for each column values.
    :type  test_case_title_cells_row: int
    :param test_case_param_name_cells_row: Row number of the parameter name cells for Pydoc inner comments function each function inputs.
    :type  test_case_param_name_cells_row: int
    :param test_case_param_type_cells_row: Row number of the parameter type cells for Pydoc inner comments function each function inputs.
    :type  test_case_param_type_cells_row: int
    :param test_case_param_description_cells_row: Row number of the parameter description cells for Pydoc inner comments function each function inputs.
    :type  test_case_param_description_cells_row: int

    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return cur_test_case_function_str: The final string of current single case test case function code, which contains Pydoc inner comments, function definition and test case function body implemented.
    :rtype  cur_test_case_function_str: string
    """
    # init test case element variables
    test_case_id = ""
    test_case_title = ""
    test_case_description = ""
    test_case_class_name = ""
    test_case_function_name = ""
    test_case_testing_function_return_type = ""
    test_case_variable_name = ""

    code_lines_before_function_body_str = ""
    code_lines_after_function_body_str = ""

    #===========================================================================
    # Process current test case function 
    #===========================================================================
    # index 0: Test Case ID - Get test case ID for current case
    test_case_id = spreadsheetData[rowIndex][0]
    # index 1: Test case title
    test_case_title = spreadsheetData[rowIndex][1]
    # index 2: Test case description
    test_case_description = spreadsheetData[rowIndex][2]
    # index 3: Testing class name
    test_case_class_name = spreadsheetData[rowIndex][3]
    # index 4: Testing function name
    test_case_function_name = spreadsheetData[rowIndex][4]
    # index 5: Testing function return type
    test_case_testing_function_return_type = spreadsheetData[rowIndex][5]
    # index 6: Testing variable name
    test_case_variable_name = spreadsheetData[rowIndex][6]

    # index 7 ...: Param - Get all the function paramter inputs
    test_case_class_obj_allocation_param_starting_index = 7
    test_case_class_testing_function_input_param_starting_index = 0
    test_case_class_testing_function_expected_output_starting_index = 0
    #===========================================================================
    # Reset current test case local data
    #===========================================================================
    # Parameters needed to allocate the testing class object before testing the 
    # class, and is also used to test the __init__ constructors.
    test_case_class_obj_allocation_param_arr = []
    test_case_class_obj_allocation_param_arr_counter = 0

    # Parameters passed into the testing function call.
    test_case_class_testing_function_input_param_arr = []
    test_case_class_testing_function_input_param_arr_counter = 0

    # Expected output for current test case testing function.
    test_case_class_testing_function_expected_result_arr = []
    test_case_class_testing_function_expected_result_arr_counter = 0

    # The lines of codes to be prepended before the function body 
    # implementation.
    code_lines_before_function_body_str = ""
    code_lines_before_function_body_col_index = 0

    # The lines of codes to be appended after the function body 
    # implementation.
    code_lines_after_function_body_str = ""
    code_lines_after_function_body_col_index = 0

    # The full testing function body implementation code.
    test_case_function_body_full_code_str = ""
    test_case_function_body_full_code_exist = False
    test_case_function_body_full_code_col_index = 0

    if test_case_title_cells_row > 0:
        index = test_case_class_obj_allocation_param_starting_index
        # if current column is testing class object allocation paramters column ...
        while spreadsheetData[test_case_title_cells_row][index].find("Alloc param") != -1 :
            # Append the testing class object allocation parameter data 
            # for current test case
            test_case_class_obj_allocation_param_arr.append(spreadsheetData[rowIndex][index])
            test_case_class_obj_allocation_param_arr_counter += 1
            index += 1

        test_case_class_testing_function_input_param_starting_index = index
        # if current column is testing function input paramter column ...
        while spreadsheetData[test_case_title_cells_row][index].find("Func param") != -1 :
            # Append the testing function input parameter data 
            # for current test case
            test_case_class_testing_function_input_param_arr.append(spreadsheetData[rowIndex][index])
            test_case_class_testing_function_input_param_arr_counter += 1
            index += 1
        
        test_case_class_testing_function_expected_output_starting_index = index
        # index .. Followed by input parmater columns: 
        # Expected Result - Get all the function expected 
        while spreadsheetData[test_case_title_cells_row][index].find("Expected result") != -1 :
            if index < len(spreadsheetData[rowIndex]):
                # Append the expected data for current 
                # test case
                #print("spreadsheetData[rowIndex][index]: ", spreadsheetData[rowIndex][index])
                if spreadsheetData[rowIndex][index] != "":
                    test_case_class_testing_function_expected_result_arr.append(spreadsheetData[rowIndex][index])
                    test_case_class_testing_function_expected_result_arr_counter += 1
            index += 1

        while spreadsheetData[test_case_title_cells_row][index].find("Test case data lists note") != -1 :
            index += 1
        while spreadsheetData[test_case_title_cells_row][index].find("Note") != -1 :
            index += 1

        # index .. Followed by expected result + test case data note
        # Code lines before testing body - 
        #   Codes that will be prepended before the testing function body
        code_lines_before_function_body_col_index = index
        if code_lines_before_function_body_col_index < len(spreadsheetData[rowIndex]) and \
            spreadsheetData[test_case_title_cells_row][code_lines_before_function_body_col_index].find("Code lines before testing body") != -1:
            #print("Code lines before testing body:", spreadsheetData[rowIndex][code_lines_before_function_body_col_index])
            code_lines_before_function_body_str = str(spreadsheetData[rowIndex][code_lines_before_function_body_col_index])
        
        # index .. Followed by the codes lines before testing body column: 
        # Code lines after testing body - 
        #   Codes that will be appended after the testing function body
        code_lines_after_function_body_col_index = code_lines_before_function_body_col_index + 1
        if code_lines_after_function_body_col_index < len(spreadsheetData[rowIndex]) and \
           spreadsheetData[test_case_title_cells_row][code_lines_after_function_body_col_index].find("Code lines after testing body") != -1:
            #print("Code lines after testing body:", spreadsheetData[rowIndex][code_lines_after_function_body_col_index])
            code_lines_after_function_body_str = str(spreadsheetData[rowIndex][code_lines_after_function_body_col_index])

        test_case_function_body_full_code_col_index = code_lines_after_function_body_col_index + 1
        if test_case_function_body_full_code_col_index < len(spreadsheetData[rowIndex]) and \
           spreadsheetData[test_case_title_cells_row][len(spreadsheetData[rowIndex])-1].find("Test case funciton body full code") != -1:
            if spreadsheetData[rowIndex][len(spreadsheetData[rowIndex])-1] != "":
                #print("Test case funciton body full code:", spreadsheetData[rowIndex][len(spreadsheetData[rowIndex])-1])
                test_case_function_body_full_code_str = str(spreadsheetData[rowIndex][len(spreadsheetData[rowIndex])-1])
                test_case_function_body_full_code_exist = True


    #print("=========================================================================")
    #print("test_case_id                     : " +  test_case_id)
    #print("=========================================================================")
    #print("test_case_id                                                                     : " + test_case_id)
    #print("test_case_title                                                                  : " + test_case_title)
    #print("test_case_description                                                            : " + test_case_description)
    #print("test_case_class_name                                                             : " + test_case_class_name)
    #print("test_case_function_name                                                          : " + test_case_function_name)
    #print("test_case_testing_function_return_type                                                   : " + test_case_testing_function_return_type)
    #print("test_case_variable_name                                                          : " + test_case_variable_name)
    #print("test_case_class_obj_allocation_param_arr                                         : " + str(test_case_class_obj_allocation_param_arr))
    #print("test_case_class_obj_allocation_param_arr_counter                                 : " + str(test_case_class_obj_allocation_param_arr_counter))
    #print("test_case_class_obj_allocation_param_starting_index                              : " + str(test_case_class_obj_allocation_param_starting_index))
    #print("test_case_class_testing_function_input_param_arr                                 : " + str(test_case_class_testing_function_input_param_arr))
    #print("test_case_class_testing_function_input_param_arr_counter                         : " + str(test_case_class_testing_function_input_param_arr_counter))
    #print("test_case_class_testing_function_input_param_starting_index                      : " + str(test_case_class_testing_function_input_param_starting_index))
    #print("test_case_class_testing_function_expected_result_arr                             : " + str(test_case_class_testing_function_expected_result_arr))
    #print("test_case_class_testing_function_expected_result_arr_counter                     : " + str(test_case_class_testing_function_expected_result_arr_counter))
    #print("test_case_class_testing_function_expected_output_starting_index                  : " + str(test_case_class_testing_function_expected_output_starting_index))


    #===========================================================================
    # Get current test case function Pydoc docstring
    #===========================================================================
    cur_test_case_function_pydoc_str = ""
    cur_test_case_function_pydoc_str = sub_process_data_generate_test_case_function_pydoc(spreadsheetData, 
                                     test_case_id, test_case_title, test_case_description, 
                                     test_case_class_name, test_case_function_name, test_case_testing_function_return_type, test_case_variable_name, 
                                     test_case_class_obj_allocation_param_arr, test_case_class_obj_allocation_param_arr_counter, test_case_class_obj_allocation_param_starting_index, 
                                     test_case_class_testing_function_input_param_arr, test_case_class_testing_function_input_param_arr_counter, test_case_class_testing_function_input_param_starting_index,
                                     test_case_class_testing_function_expected_result_arr, test_case_class_testing_function_expected_result_arr_counter, test_case_class_testing_function_expected_output_starting_index,
                                     test_case_param_name_cells_row, test_case_param_type_cells_row, test_case_param_description_cells_row)
    
    #===========================================================================
    # Generate current test case function unit test case string where Pydoc is 
    # also implemented inside the function string
    #===========================================================================
    cur_test_case_function_str = ""
    cur_test_case_function_str = sub_process_data_generate_test_case_function(spreadsheetData, 
                                    cur_test_case_function_pydoc_str,
                                    test_case_id, test_case_title, test_case_description, 
                                    test_case_class_name, test_case_function_name, test_case_testing_function_return_type, test_case_variable_name, 
                                    test_case_class_obj_allocation_param_arr, test_case_class_obj_allocation_param_arr_counter, test_case_class_obj_allocation_param_starting_index, 
                                    test_case_class_testing_function_input_param_arr, test_case_class_testing_function_input_param_arr_counter, test_case_class_testing_function_input_param_starting_index,
                                    test_case_class_testing_function_expected_result_arr, test_case_class_testing_function_expected_result_arr_counter, test_case_class_testing_function_expected_output_starting_index,
                                    code_lines_before_function_body_str, code_lines_after_function_body_str,
                                    test_case_param_name_cells_row, test_case_param_type_cells_row, test_case_param_description_cells_row,
                                    test_case_function_body_full_code_exist, test_case_function_body_full_code_str)

    # Return generated current Python unit test case function code string.
    return cur_test_case_function_str

def process_google_spreadsheet_test_case_data(spreadsheetData):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Test cases generator sub function to help generating the unit test cases.

    Called by function  : oauth_test_case_generator_generator::oauth_test_case_generator_generator()
    Calling sub function: sub_process_data_generate_current_test_case_function_str()
    Calling sub function: sub_process_data_generate_test_case_file_header()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function processes the spreadsheet data retrieved from Google 
    Spreadsheet and read the data value by cells, and generates the Python 
    unit test cases string and write them into each testing class folder's 
    test cases folder.

    Sub function: sub_process_data_generate_current_test_case_function_str()
                  Return the test case function string for each cases indicated 
                  by each spreadsheet row.
    Sub function: sub_process_data_generate_test_case_file_header()
                  Return the unit test case file header including extra library 
                  import codes and unit test case class definition and Pydoc 
                  inner comment codes.
    Util function: safe_open_w()
                   This util function creates the directory if the file path 
                   does not exits, which means the file will be generated even 
                   though the path does not exist.
    
    First generate the unit test case file header which will be implemented at 
    the very top of each unit test cases.
                  
    Then using each test case function generated from sub function with each 
    spreadsheet row data values, i can combine them into multiple test case 
    functions string to be appeneded to the unit test case file header string.

    At the end, I append the main function code string for unit test case 
    execution.

    Then save the file onto each proper destinations using the utility function.

    Return the unit test case file path to execute it and also the file path to
    store the execution results. 
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param spreadsheetData: Google Spreadsheet data list data structure.
    :type  spreadsheetData: [[],[],[] ...]
    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return final_path_list: List data structure containing 
                                Index 0 : the final generated unit test case file path,
                                Index 1 : the absolute path of the file to store the result of the unit test cases results.
    :rtype  final_path_list: []
    """
    # Final string variables
    spreadsheet_data_log_str = ""

    final_test_case_file_str = ""
    final_test_case_main_title_str = ""
    final_test_case_header_str = ""
    final_test_case_functions_str = ""
    final_test_case_execution_code_str = ""

    cur_test_case_function_str = ""

    # Special data rows
    test_case_title_cells_row = 0
    test_case_param_name_cells_row = 0
    test_case_param_type_cells_row = 0
    test_case_param_description_cells_row = 0

    # Test case summary values
    test_case_normal_case_counter = 0
    test_case_boundary_case_counter = 0
    test_case_error_case_counter = 0
    test_case_white_box_counter = 0
    test_case_black_box_counter = 0

    # Project title element variables
    test_case_proj_name = ""
    test_case_date_of_creation = ""
    test_case_last_update = ""
    test_case_created_by = ""
    test_case_testing_class_file_name = ""
    test_case_file_name = ""
    test_case_data_file_name = ""
    test_case_testing_class_function_name = ""
    
    test_case_unittestcase_class_name = ""
    test_case_unittestcase_class_description = ""
    test_case_unittestcase_class_header_imports = ""
    test_case_unittestcase_result_file_name = ""
    # Load spreadsheet data line by line for data counting
    for i in range(0, len(spreadsheetData)):
        spreadsheet_data_log_str += str(spreadsheetData[i]) + "\n"
        if len(spreadsheetData[i]) > 0:
            #===================================================================
            # Title
            #===================================================================
            # Load informations about this test cases
            if spreadsheetData[i][0] == "Project name":
                test_case_proj_name = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Date of creation":
                test_case_date_of_creation = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Last update":
                test_case_last_update = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Created by":
                test_case_created_by = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Test case file name":
                test_case_file_name = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Test case data file name":
                test_case_data_file_name = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Testing class file name":
                test_case_testing_class_file_name = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Testing class function name":
                test_case_testing_class_function_name = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Unit test case class name":
                test_case_unittestcase_class_name = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Unit test case class description":
                test_case_unittestcase_class_description = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Unit test case class header imports":
                test_case_unittestcase_class_header_imports = spreadsheetData[i][1]
            if spreadsheetData[i][0] == "Unit test case result file name":
                test_case_unittestcase_result_file_name = spreadsheetData[i][1]

            #===================================================================
            # Special row numers
            #===================================================================
            # Get title cells row number
            if spreadsheetData[i][0].find("NC - Test Case ID") != -1:
                # The row where all the column titles cells are indicated
                test_case_title_cells_row = i
                #print("test_case_title_cells_row      : " +  str(test_case_title_cells_row))
            # Get input param name cells row number
            if "Param name" in spreadsheetData[i]:
                # The row where input paramter names cells are indicated
                test_case_param_name_cells_row = i
                #print("test_case_param_name_cells_row : " +  str(test_case_param_name_cells_row))
            # Get input param type cells row number
            if "Param type" in spreadsheetData[i]:
                # The row where input paramter types cells are indicated
                test_case_param_type_cells_row = i
                #print("test_case_param_type_cells_row : " +  str(test_case_param_type_cells_row))
            # Get input param description cells row number
            if "Param description" in spreadsheetData[i]:
                # The row where input paramter descriptions are indicated
                test_case_param_description_cells_row = i
                #print("test_case_param_description_cells_row : " +  str(test_case_param_description_cells_row))

            #===================================================================
            # Summary counters
            #===================================================================
            if (spreadsheetData[i][0].find("TC_NC") != -1): test_case_normal_case_counter += 1 
            if (spreadsheetData[i][0].find("TC_BC") != -1): test_case_boundary_case_counter += 1
            if (spreadsheetData[i][0].find("TC_EC") != -1): test_case_error_case_counter += 1
            if (spreadsheetData[i][0].find("TC_WX") != -1): test_case_white_box_counter += 1
            if (spreadsheetData[i][0].find("TC_BX") != -1): test_case_black_box_counter += 1

            #===================================================================
            # Start loading test cases and generate test case function string 
            # for each cases using the data where first column value has "TC_NC"
            # or "TC_EC" string inside, which means each row is representing a
            # test case with unique test case id
            #===================================================================
            cur_test_case_function_str = ""
            if spreadsheetData[i][0].find("TC_NC") != -1 or spreadsheetData[i][0].find("TC_EC") != -1:
                # Process current function data into test case string
                cur_test_case_function_str = sub_process_data_generate_current_test_case_function_str(spreadsheetData, i, test_case_title_cells_row, 
                                            test_case_param_name_cells_row, test_case_param_type_cells_row, test_case_param_description_cells_row)

            # Add current test case function string to final test cases string
            final_test_case_functions_str += cur_test_case_function_str
            #print("=========================================================================")

    #===========================================================================
    # Generate test case string 
    #===========================================================================
    final_test_case_main_title_str  += "\"\"\"" + "\n"
    final_test_case_main_title_str  += "Project name                        : " + test_case_proj_name + "\n"
    final_test_case_main_title_str  += "Date of creation                    : " + test_case_date_of_creation + "\n"
    final_test_case_main_title_str  += "Last update                         : " + test_case_last_update + "\n"
    final_test_case_main_title_str  += "Created by                          : " + test_case_created_by + "\n"
    final_test_case_main_title_str  += "Test case file name                 : " + test_case_file_name + "\n"
    final_test_case_main_title_str  += "Test case data file name            : " + test_case_data_file_name + "\n"
    final_test_case_main_title_str  += "Testing class file name             : " + test_case_testing_class_file_name + "\n"
    final_test_case_main_title_str  += "Testing class function name         : " + test_case_testing_class_function_name + "\n"
    final_test_case_main_title_str  += "Unit test case class name           : " + test_case_unittestcase_class_name + "\n"
    final_test_case_main_title_str  += "Unit test case description          : " + test_case_unittestcase_class_description + "\n"
    final_test_case_main_title_str  += "Unit test case result file name     : " + test_case_unittestcase_result_file_name + "\n"
    
    final_test_case_main_title_str  +=  "\"\"\"" + "\n"
   
    final_test_case_header_str = sub_process_data_generate_test_case_file_header(test_case_unittestcase_class_header_imports,
                                                test_case_testing_class_file_name, test_case_unittestcase_class_name, test_case_unittestcase_class_description,
                                               test_case_normal_case_counter, test_case_boundary_case_counter, test_case_error_case_counter, 
                                               test_case_white_box_counter, test_case_black_box_counter)

    #===========================================================================
    # Unit test case main function definition
    #===========================================================================
    final_test_case_execution_code_str += "\nif __name__ == '__main__':" + "\n"
    final_test_case_execution_code_str += "    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(" + test_case_unittestcase_class_name + "))" + "\n"

    #===========================================================================
    # Manipulate the final test case file string by concatting
    #   Final test case title string
    #   Final test case string (All test case function strings)
    #===========================================================================
    final_test_case_file_str += final_test_case_main_title_str
    final_test_case_file_str += final_test_case_header_str
    final_test_case_file_str += final_test_case_functions_str
    final_test_case_file_str += final_test_case_execution_code_str

   
    #===========================================================================
    # Write the spreadsheet data retrieved from Google into text file
    #===========================================================================
    with safe_open_w(test_case_data_file_name) as text_file:
        text_file.write(spreadsheet_data_log_str)
    #===========================================================================
    # Write the test case file with the test case file string generated
    # from above
    #===========================================================================
    current_working_directory = os.getcwd()
    with safe_open_w(test_case_file_name) as text_file:
        text_file.write(final_test_case_file_str)
        final_generated_test_case_file_abs_path = current_working_directory + "\\" + test_case_file_name

    final_unittestcase_exe_result_file_abs_path = current_working_directory + "\\" +  test_case_unittestcase_result_file_name
    
    #===========================================================================
    # Return a list containing 
    #  1. Final generated test case file absolute path to check if it is 
    #     generated properly before executing them.
    #  2. The absolute path to store the unit test case execution result output.
    #===========================================================================
    return [final_generated_test_case_file_abs_path, final_unittestcase_exe_result_file_abs_path]

#===============================================================================
#===============================================================================
#===============================================================================
# Sub main function
# Code brought from: https://developers.google.com/sheets/api/quickstart/python 
#===============================================================================
#===============================================================================
#===============================================================================
def oauth_test_case_generator_generator(google_spreadsheet_url, scopes,
                                oauth_client_application_name, oauth_client_secret_json_file,
                                feed_name, feed_range):
    """
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Test case generator which generates the unit test case file with data 
    values provided within the Google Spreadsheet.

    Called by function  : oauth_test_case_generator_manager::main()
    Calling sub function: oauth_test_case_generator_get_spreadsheet_data::oauth_test_case_generator_get_spreadsheet_data()
    Calling sub function: process_google_spreadsheet_test_case_data()
        Calling sub function: sub_process_data_generate_current_test_case_function_str()
            Calling sub function: sub_process_data_generate_test_case_function()
            Calling sub function: sub_process_data_generate_test_case_function_pydoc()
        Calling sub function: sub_process_data_generate_test_case_file_header()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function processes the data retrieved from provided Google Spreadsheet
    and generates the Python unit test cases into each class folders.

    Sub function: oauth_test_case_generator_get_spreadsheet_data()
                  Return the spreadsheet data in Python list data structure 
                  format for easier computes.
    Sub function: process_google_spreadsheet_test_case_data()
                  This function generates the unit test case file and return the 
                  unit test case file path to execute it and also the file path
                  to store the execution results. 

    Note: All the important informations are provided in the Google Spreadsheet
          test case data files.
          See: [ ./oauth_test_case_generator_spreadsheet_sample_template.xlsx ]
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
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param google_spreadsheet_url: Google Spreadsheet URL to retrieve the data from.
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
    :return final_path_list: List data structure containing 
                                Index 0 : the final generated unit test case file path,
                                Index 1 : the absolute path of the file to store the result of the unit test cases results.
    :rtype  final_path_list: []
    """

    # Get Google spreadsheet data using sub function from script oauth_test_case_generator_get_spreadsheet_data.py
    spreadsheetData = oauth_test_case_generator_get_spreadsheet_data(google_spreadsheet_url, scopes,
                                oauth_client_application_name, oauth_client_secret_json_file,
                                feed_name, feed_range)

    # Parse spreadsheet data retrieved
    if not spreadsheetData:
        print('No data found.')
    else:
        # Get rid of empty lists inside the spreadsheet data list
        spreadsheetData = [x for x in spreadsheetData if x != []]
        # Using the data retrieved from Google spreadsheet to generate Python
        # unit test cases and then generate the test case file and return the 
        # list of generated test case file paths.
        final_path_list = process_google_spreadsheet_test_case_data(spreadsheetData)
    
    # Return a list containing 
    #  1. Final generated test case file absolute path to check if it is 
    #     generated properly before executing them.
    #  2. The absolute path to store the unit test case execution result output.
    return final_path_list

   
