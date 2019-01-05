================================================================================
                                    READ ME
================================================================================
Project name: 
    - WY_PROJ_BLENDER_EDITOR.
    - Project was originally brought from 
      [ BlenderExporterImporterProj_ver0055 ].

Objectives:
    - Understanding of game editor framework and mechanism by creating 
      custom exporter and importers using Blender API to export and import
      Blender mesh, material, armature and animation to files and load 
      them to my custom engine.  

Staff:
    - Junior programmer : Nick Jang.

Old project: [BlenderExporterImporter]
    Start date	  : 2017-04-15
    End date  	  : 2017-09-20
    Partial dates :
	Intro			: 2017-04-15 - 2017-04-27
	Mesh			: 2017-04-22 - 2017-04-23
	Material		: 2017-04-23 - 2017-04-27
	Coordinate conversion	: 2017-04-24 - 2017-04-30
	Armature		: 2017-07-11 - 2017-07-13
	Animation		: 2017-07-13 - 2017-09-20

Current project: [WY_PROJ_BLENDER_EDITOR]
    Start date	  : 2017-09-20
    End date  	  : 2017-10-31
    Partial dates :
	Pydoc Blender setup		: 2017-09-26 - 2017-10-01
	Oauth with Python		: 2017-10-02 - 2017-10-02
	Python Argparse			: 2017-10-02 - 2017-10-02
	Python test case generator	: 2017-10-02 - 2017-10-03
	Install batch			: 2017-10-13 - 2017-10-20

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
    - Windows 10 64 bits compatible:
        - CMake 		Version 3.9.4 	Windows 10 x64.
        - Git   		Version 2.14.1 	Windows 10 x64.
        - SVN   		Version 1.9.7 	Windows 10 x64.
        - Visual Studio 2017  	Version 3.9.4 	Windows 10 x64.
        - Python 		Version 3.6.2	Windows 10 x64.
        - Blender module	Version Trunk	Windows 10 x64.
Techique used:
    - Python/Blender Python API.

Sources:
    Code was originally brought from [ BlenderExporterImporterProj_ver0055 ].

Project documents Google Drive folder:
    - Google drive : [ https://docs.google.com/document/d/
 		       1cJZ_oUeUo8GUkbYIRbQfX-5pHTvovKU1wq_U0l9Lelw/edit# ].

Project document headquarter:
    - Google docs : [ https://docs.google.com/document/d/
		      1B_V9Rhkh17cy4JNlMqg02RBvVt1FgdOZuMK9LYTWjt0/edit ]. 
	
How to run:
    WARNING:
	The project is incompleted due to creating tools as sub projects
	supporting mesh and material exporter developing, where one sub
	project is a Python test case generator with OAuth which generates 
	the Python unit test cases using the test case data retrieved from 
	Google Spreadsheet and another one is a HTML time report dashboard
	generator with Python which also using the data retrieved from 
	Google Spreadsheet using OAuth.

	But can test the tool created as sub projects of the mesh and material
	exporter by following the user guide in each sub projects directory
	inisde "MESH_MAT_EXPORTER/" which test case generator sub project 
	is called "OAuthTestGenerator" and the time report dashboard sub 
 	project is called "OAuthTimeReportDashboard"

Note: 
    - This project was originally developed as project name 
      [ BlenderExporterImporterProj ] where all the document 
      are combined within the main DirectX 12 project's document 
      [ WY_PROJ_DIRECTX_12_WIN32 ] so the HQ and the detail document is 
      combined inside the DirectX 12 project's HQ document 
      [ https://docs.google.com/document/d/
	1B_V9Rhkh17cy4JNlMqg02RBvVt1FgdOZuMK9LYTWjt0/edit ]

    - This project was originally developed without specific and 
      separated stand alone documents, refactoring, API, 
      diagrams and test cases, which was called [ BlenderExporterImporterProj ]
      where I continue to developing multiple 
      custom exporter and importers such as for meshes, 
      materials, armatures and animations.

================================================================================
Directory description:
================================================================================
EXTRA_DOCUMENTS/	Documents for Git setup guide
			Documents for Blender coordinate system conversion 
			mechanism spreadsheet documents.
MAIN/			Main mesh and material exporter project directory.
			documents.

WY_PROJ_BLENDER_EDITOR.sln
			Visual Studio IDE project explorer solution file.



