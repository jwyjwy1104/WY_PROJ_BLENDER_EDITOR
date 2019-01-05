================================================================================
                                    READ ME
================================================================================
Project name: 
    - OAuthTimeReportDashboard.

Objectives:
    - To analyze my risk management and time mangement I needed a tool to 
      observe my daily process by checking work efficiency, total working 
      time and final working time in graph state which is the best way to 
      visualize a process in certain period of time.
      Using OAuth to retrieve the data from Google Spreadsheet time reports 
      and generate a HTML page which shows a graph which time reports data 
      are pushed into the graph, and this graph is drawn with external 
      Javascript library called amChart.js.

Staff:
    - Lead programmer   : Samil Chai.
    - Junior programmer : Nick Jang.
    - [ Copy right to Samil Chai ]

Start date: 2017-10-08
End date  : 2017-10-12

Environment:
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
    - HTML5/Javascript/amChart/
    - Python/Argparse/Python subprocess/
    - Pydoc/OAuth 2.0/Google Developer Console.

Project documents Google Drive folder:
    - Google drive : [ https://drive.google.com/drive/folders/
		       0B8vIEi2xiwB4RGxkVHhxWlIzMTQ ].

Project document headquarter:
    - Google docs : [ https://docs.google.com/document/d/
		      1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit# ]. 
	
How to run:
    -
================================================================================
Project directory description:
================================================================================
client_secret.json	OAuth client secret file for authentication.
Diagrams/		Collection of important algorithm diagrams.
Documents/		Collection of important algorithm setup guide, 
			framework and documents.
API/			Where the Pydoc HTML pages generated for all the 
			scripts used in this tool are stored.
makefile		Main makefile to compile and run the OAuth time 
			report dashboard generator. All the spreadsheet URL 
			will be indicated inside this makefile to manage them 
			in one place. Also the Pydoc for all the scripts used
			in this tool are generated into HTML pages inside the 
			folder "API".
moment.js		Third party library used for date object format 
			conversions and comparisons.
oauth_time_report_dashboard_generator.py			
			Sub Python script that processes the Google spreadsheet
			data and generates the time report dashboard HTML file.
oauth_time_report_dashboard_get_spreadsheet_data.py	
			Sub Python script that authenticate with Google 
			Developer Console API to get the OAuth credential to 
			access the Google Spreadsheet to retrieve the data 
			from the Google spreadsheet with given URL.
oauth_time_report_dashboard_util.py			
			Sub Python script that organizes the utility functions
			to help processing the spreadsheet data to generate 
			the time report dashboard.
oauth_time_report_dashboard_manager.py			
			Main Python script that manages all the subscripts 
			in one place to organize the framework. This is the main 
			script to be called in makefile to generate the time 
			report dashboard HTML files. After the execution of this 
			script, the result will be the followings:
				Time report dashboard HTML page generated.
				All Python scripts Pydoc HTML page generated.
oauth_time_report_dashboard_spreadsheet_template.xlsx
			Sample Google Spreadsheet time report template 
			downloaded in Microsoft Excel format.	






