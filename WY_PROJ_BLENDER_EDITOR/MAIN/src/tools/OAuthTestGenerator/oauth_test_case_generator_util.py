import errno
import os, os.path

def mkdir_p(path):
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Sub function to create the directory if given file path does not exist.

    Called by function: oauth_time_report_dashboard_util::safe_open_w()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function opens up a file with provided file path, but if the directory
    containing current file does not exist then i create the directory and then 
    opens up the file.

    In this way, I can safely open up any file path given even though the 
    directory path does not exist.
    ------------------------------------------------------------------------
    Resources:
    ------------------------------------------------------------------------
    Code brought from https://stackoverflow.com/a/600612/119527
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param path: File path to open with.
    :type  path: string
    '''
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    ''' 
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Utility function to create the directory if given file path does not exist.

    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function opens up a file with provided file path, but if the directory
    containing current file does not exist then i create the directory and then 
    opens up the file.

    In this way, I can safely open up any file path given even though the 
    directory path does not exist.
    ------------------------------------------------------------------------
    Resources:
    ------------------------------------------------------------------------
    Code brought from https://stackoverflow.com/a/600612/119527

    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param path: File path to open with.
    :type  path: string
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')

def save_list_to_file(file_path, saving_list):
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Utility function to save the list data structure into text file with 
    byte codes.

    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function opens up with the file path given and write the provided list 
    data structure into the file as byte code opened up with "wb" where 'b' 
    indicates "byte" and "w" indicates "write".
    
    Example:
        This function is created to merge the multiple list data structure data  
        when generating time report dashboard for multiple Google Spreadsheet  
        time reports, so i can merge the data with 2 different execution call.

    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param file_path: File path to export the list data structure into byte codes.
    :type  file_path: string
    :param saving_list: List data structure to save as byte code into a text file.
    :type  saving_list: []
    '''
    # Open file path with "wb" byte code option and write the list object onto 
    # the file
    with open(file_path, "wb") as text_file:
        pickle.dump(saving_list, text_file)

def load_list_from_file(file_path):
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Utility function to load the list data structure from the text file with 
    byte codes.

    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function opens up with the file path given and load the list 
    data structure read as byte code from the file path provided, the file is
    opened up with "rb" where 'b' indicates "byte" and "r" indicates "read".
    
    Example:
        This function is created to merge the multiple list data structure data  
        when generating time report dashboard for multiple Google Spreadsheet  
        time reports, so I can merge the data with 2 different execution call.

    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param file_path: File path to load the list data structure byte codes from.
    :type  file_path: string
    '''
    # Check if file exist
    if os.path.isfile(file_path):
        # Load list data structure from byte code text file
        with open(file_path, "rb") as text_file:
            # Load list with pickle library
            loaded_list = pickle.load(text_file)
        # Return the loaded list if successful
        return loaded_list
    else:
        # Raise exception if failed
        raise ValueError('oauth_time_report_dashboard_util::load_list_from_file::File not loaded')

def find_element_in_list_with_key_in_lists(lists, finding_elem, key):
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Utility function to help processing the Google Spreadsheet data into 
    Python list format.

    Called by function: oauth_time_report_dashboard_generator::process_google_spreadsheet_time_report_data_into_amchart_data()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function iterates through the provided list and finds the provided 
    element with provided key and return the found element else return None.

    Example:
        This function is used to find the same time report data which has the  
        same date so the data won't be duplicated in the data structure.
        
        find_element_in_list_with_key_in_lists([{date:"10/07"},{date:"10/08"},{date:"10/09"}], {date: "10/17"}, "date")
        --> Return {date:"10/07"}
        find_element_in_list_with_key_in_lists([{date:"10/07"},{date:"10/08"},{date:"10/09"}], {date: "10/17"},"date")
        --> Return None

    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param lists: Main data structure to find the element with.
    :type  lists: [{},{},{} ... ]
    :param finding_elem: Element value to find inside the data structure.
    :type  finding_elem: {}
    :param key: String key value to find the matching element.
    :type  key: String

    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return None: If element is not found in the list with provided key.
    :rtype  None: None
    :return list_elem: The element found in the list with provided key.
    :rtype  list_elem: {} 
    '''

    for list_elem in lists:
        if list_elem[key] == finding_elem:
            return list_elem
    return None

def validate_date_string_format(date_text):
    '''
    ------------------------------------------------------------------------
    Title:
    ------------------------------------------------------------------------
    Utility function to help validating the Google Spreadsheet cell string is
    matching date value format "0000/00/00"

    Called by function: oauth_time_report_dashboard_generator::process_google_spreadsheet_time_report_data_into_amchart_data()
    ------------------------------------------------------------------------
    Description:
    ------------------------------------------------------------------------
    This function checks whether the string value passed in as parameter is 
    matching date value format "0000/00/00"

    Example:
        validate_date_string_format("2017/10/11") --> Return True
        validate_date_string_format("2017/10-11") --> Return False
        validate_date_string_format("2017-10-11") --> Return False
        validate_date_string_format("2017.10.11") --> Return False
        
    ------------------------------------------------------------------------
    Parameters:
    ------------------------------------------------------------------------
    :param date_text: String value to test the format with.
    :type  date_text: string

    ------------------------------------------------------------------------
    Return:
    ------------------------------------------------------------------------
    :return: True if string matches the date format "0000/00/00".
    :return: False if string does not matches the date format "0000/00/00".
    '''
    try:
        # Compare string format
        datetime.strptime(date_text, '%Y/%m/%d')
        return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY/MM/DD")
        return False