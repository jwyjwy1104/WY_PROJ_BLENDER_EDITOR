# WYCOORDSYS_TESTCASE_FINAL_RESULT_FILE_PATH := ${CURDIR}/../WYCoordsys/WYCoordsysTestCaseResults.txt
# > $(WYCOORDSYS_TESTCASE_FINAL_RESULT_FILE_PATH)

#===============================================================================
all:
#===============================================================================
#       ------------------------------------------------------------------------
#       Delete all files need to be updated
#       ------------------------------------------------------------------------
	make clean
	
#       ========================================================================
# 	[ WY_PROJ_BLENDER_EDITOR_06_20171008_20171010_TIME_REPORT  ] 
#       ========================================================================
	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_06_20171008_20171010_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1ur-DnfW33Nb9iySsvpyhN_mOajdO8ZDNEavJfv5UI9A/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"

	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_05_20171004_20171007_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1gfK3k5pRZ90hTjVGyoLRa5-0dXa6wT5olaiRwDUwnys/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"
#	> ./result.txt

	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_04_20171001_20171004_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1WReZYyjIMcfau-9TfERLZtquK7Tx1kRhHKCTfv1u184/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"

	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_03_20170928_20171001_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1E0NlrEKegFmiFqvOzV09CB8DRSArCfFB9UfZzCwPly8/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"

	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_02_20170926_20170928_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1KHwsZxAWWnmn_-7Xk7oRgdhsRT0NmHLYguOe-V_hsxw/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"

	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_01_20170914_20170919_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1Teg5qWBgj0zLlwy8z4Upi4kEMIiyd8n3onzt2tuYc50/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"

	python oauth_time_report_dashboard_manager.py \
	-title "[ WY_PROJ_BLENDER_EDITOR_07_20171011_20171014_TIME_REPORT ]" \
	-ssurl https://docs.google.com/spreadsheets/d/1Q5QrF447sRA6w_2xB0Z9YQ-xLfGqSaqtSS-T-mhZgng/edit#gid=0 \
	-feed Sheet1 \
	-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
	-filepath ".\oauth_time_report_dashboard.html"




#       ------------------------------------------------------------------------
#       Execute the dashboard HTML pages 
#       (MUST cd first because "start" only works with file name not path)
#       ------------------------------------------------------------------------
	cd ${CURDIR} & start oauth_time_report_dashboard.html

#       ------------------------------------------------------------------------
#       Generate Pydoc for time report dashboard tool
#       ------------------------------------------------------------------------
	make pydoc

#===============================================================================
pydoc:
#===============================================================================
#       Generating Pydoc with Python I can only give file names, so I generate them first and move them to the Documents folder.
	python -m pydoc -w oauth_time_report_dashboard_generator & move oauth_time_report_dashboard_generator.html ./API
	python -m pydoc -w oauth_time_report_dashboard_get_spreadsheet_data & move oauth_time_report_dashboard_get_spreadsheet_data.html ./API
	python -m pydoc -w oauth_time_report_dashboard_executor & move oauth_time_report_dashboard_executor.html ./API
	python -m pydoc -w oauth_time_report_dashboard_util & move oauth_time_report_dashboard_util.html ./API
#===============================================================================
clean:
#===============================================================================
#       Delete the main time report dashboard.
	del "oauth_time_report_dashboard.html"

#       Delete the main time report dashboard list data byte codes text files.
	del "oauth_time_report_dashboard_spreadsheet_data_list.txt"
	del "oauth_time_report_dashboard_python_amchart_data_list.txt"

#       Delete the main time report dashboard script Pydoc HTML pages.
	cd API & del "oauth_time_report_dashboard_manager.html"
	cd API & del "oauth_time_report_dashboard_generator.html"
	cd API & del "oauth_time_report_dashboard_get_spreadsheet_data.html"
	cd API & del "oauth_time_report_dashboard_util.html"
	cd API & del "oauth_time_report_dashboard_executor.html"

