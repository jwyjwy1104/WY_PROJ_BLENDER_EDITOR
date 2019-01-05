================================================================================
                                    READ ME
================================================================================
Project name: 
    - OAuthTestGenerator.

Objectives:
    - To generate the standard test cases which has a lot of redundant or 
      works and duplication of the test case codes and data values, I needed 
      a test case generator tool to save my time of implementing redundant 
      codes and duplicated unit test cases.

Staff:
    - Lead programmer   : Samil Chai.
    - Junior programmer : Nick Jang.
    - [ Copy right to Samil Chai ]

Start date: 2017-10-02
End date  : 2017-01-08

Environment:
    - Python version	    : 3.6.2
    - Python pip version    : 9.0.1
    - Blender version: 2.78 (sub 0), branch: master, commit date: 2017-02-24.
    - Microsoft Windows 10 Boot Camp with Macbook:
	- MacBook Pro 12,1 (Retina, 13-inch, Early 2015):
	    - System type   : 64-bit operating system, x64-based processor.
	    - Processor     : Intel(R) Core(TM) i5-5287U CPU @ 2.90GHz 2.90.
	    - Installed RAM : 8.00 GB.
	    - Graphics card : Intel(R0 Iris(TM) Graphics 6100.
    - Boot Camp assistant version:	
	- Version  : Boot Camp Assistant 6.1.0, Copyright © 2016 Apple Inc. 
		     All rights reserved.
	- Created  : Friday, July 15, 2016 at 11:04 PM.
	- Capacity : 250GB.
	- Bootcamp Microsoft Windows 10 64 bits Home.

Techique used:
    - Python/Argparse/Python subprocess/
    - Pydoc/OAuth 2.0/Google Developer Console/

Project documents Google Drive folder:
    - Google drive : [ https://drive.google.com/drive/folders/
		       0B8vIEi2xiwB4RGxkVHhxWlIzMTQ ].

Project document headquarter:
    - Google docs : [ https://docs.google.com/document/d/
		      1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit# ]. 
	
How to run:
    - Refer to USER_GUIDE.txt
================================================================================
DO NOT TOUCH:
================================================================================
main.bat
client_secret.json

================================================================================
Project directory description:
================================================================================


client_secret.json	OAuth client secret file for authentication.
Diagrams/		Collection of important algorithm diagrams.
Documents/		Collection of important algorithm setup guide, 
			framework and documents

API/			Where the Pydoc HTML pages generated for all the 
			scripts used in this tool are stored.

main.bat
			Batch file to read the data indicated in the 
			data.config file and genrates the makefile for
			each classes to be exeucted to generate the unit 
			test cases for each classes implemented in the 
			data.config file. And creates the main "makefile"
			to generate and execute the test cases of which sub 
			makefiles are created.

data.config
			Data collection to generate and execute the 
			unit test cases for each classes by providing
			corresponding class member function title,
			Google Spreadsheet URL ID, sheet name and 
			class name and finally the test case result 
			text file relative path location for user 
			convenienve for using this tool.

			This file is where the user can append the data 
			values to create more unti test cases.


data_generated.txt
			This file is generated when each test cases are 
			genarted, to update the progress bar with lines
			of text appeneded to this file, so each test 
			case generation append a line of text to this 
			file for progress bar update.

			This file is generated whenever main.bat is 
			executed.

data_terminated.txt
			This file is generated whenever progress bar 
			app is terminated, this is to terminate the 
			makefile process executed in parallel whenever 
			progress bar is terminated by user.
			
			This file is deleted whenever main.bat is 
			executed.
			
makefile		Main makefile to compile and run the OAuth test 
			case generator. This makefile is created by 
			data_config_generate_make.bat.

makefile_test		
			Developig use makefile for testing single 
			OAuthTestGenerator execution.

oauth_test_case_generator_executor.py	
			Sub Python script that executes the unit test case 
			file generated from the generator, and also generates
			the HTML page for generated unit test case file.
oauth_test_case_generator_generator.py			
			Sub Python script that processes the Google spreadsheet 
			data and generates the unit test cases file.
oauth_test_case_generator_get_spreadsheet_data.py		
			Sub Python script that authenticate with Google 
			Developer Console API to get the OAuth credential to 
			access the Google Spreadsheet to retrieve the data 
			from the Google spreadsheet with given URL.
oauth_test_case_generator_util.py				
			Sub Python script that organizes the utility functions
			to help processing the spreadsheet data to generate 
			the unit test cases.
oauth_test_case_generator_manager.py			
			Main Python script that manages all the subscript calls
			in one place to organize the framework. This is the main 
			script to be called in makefile to generate the unit 
			test case files. After the execution of this script, 
			the result will be the followings:
				Unit test case generated.
				Unit test case Pydoc HTML page generated.
				Unit test case executed.
				Unit test case result output file generated.

oauth_test_case_generator_progressbar.py
			Python Tkinter progress bar app which is executed
			when main makefile is ran, to visualize the progress 
			of current project makefile process for user 
			convinience.

oauth_test_case_generator_spreadsheet_sample_template.xlsx
			Sample Google Spreadsheet test case data template 
			downloaded in Microsoft Excel format.


oauth_test_case_generator_interface.pyw
			TKinter interface for user to choose which classes to 
			generate test cases with.
			This app is executed when main.bat is executed, this 
			app generates the main makefile for this tool and 
			decides which sub makefile to be ran after all the 
			sub makefile is generated by main.bat.



OAuthTestGenerator_Failed.txt
			Collection of failed tasks by this tool.
OAuthTestGenerator_Succeeded.txt
			Collection of succeeded tasks by this tool.

data_generated.txt
			Local file to increment the progress bar tick, to show
			the user the progress processed for current tool
			execution, is generated by each makefile commands, where
			commands are generated by main.bat.

data_terminated.txt
			Local file which is generated when progress bar app is 
			terminated by user so that it can terminates the parallel 
			makefile process too.

