================================================================================
                                    READ ME
================================================================================
Project name: 
    - WY_PROJ_BLENDER_EDITOR.
    - Project was originally brought from 
      [ BlenderExporterImporterProj_ver0055 ].
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

Project description [ WY_PROJ_BLENDER_EDITOR ]:
    - This project is the collection of custom exporters and importers 
      where I can export and import the 3D models with my custom formats
      but also keeps the standard format as close as I can.
    - This project is to practice and understand the model loading and 
      exporting mechanisms and framework using Blender and Python scripts.

    - This project was originally developed without specific and 
      separated stand alone documents, refactoring, API, 
      diagrams and test cases, which was called 
      [ BlenderExporterImporterProj ]
      where i continue to developing multiple 
      custom exporter and importers such as for meshes, 
      materials, armatures and animations.

Installation guide:
    1. Click setup_win10_x64.bat 
    - This batch file installs the external program to be used for 
      project setup, these are the list of installing programs, but
      first checks if the program is installed in the system using 
      "where" command:
      1-1. ./SETUP_WIN64/install_git.bat
           Git                     - Git-2.14.1-64-bit.exe
      1-2. ./SETUP_WIN64/install_svn.bat
           SVN                     - Slik-Subversion-1.9.7-x64.msi
      1-3. ./SETUP_WIN64/install_python3.bat
           Python 3.0 higher       - python-3.6.2-amd64.exe
      1-4. ./SETUP_WIN64/install_cmake.bat
           CMake 3.9.4             - cmake-3.9.4-win64-x64.msi
      1-5. ./SETUP_WIN64/install_vs2017.bat
           Visual Studio 2017      - vs_community__1560776263.1499642898.exe

    - If any alert message box appear and terminates, means that I will have to
      install external programs before other automated installations to use
      this project.
    - If all the installations are done I can go click install_win64.bat to 
      install Blender to set up the project environment.

    2. Click install_win10_x64.bat 
    **********This might take longer than 15 minutes downloading Blender 
              source codes and libraries
    - If any alert message box appear, then there must be installations not 
      done properly. Go back to setup_win64.bat and install the mandatory 
      programs.
    - This batch file will install Blender and build the Blender 
      into module to be ported to the standard Python external modules folder
      to set up the project environment.
 
================================================================================
Project directory description:
================================================================================
WY_PROJ_BLENDER_EDITOR/		
	Main WY_PROJ_BLENDER_EDITOR project wrapper folder where main 
	installation batch file is.

    run_test.bat
	Main automated test case execution batch file which calls the 
     	make command inside the sub project "OAuthTestGenerator" inside 
	"WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\tools" folder 

    install_win10_x64_admin.bat
	Sub batch file to run install_win10_x64.bat file in admin mode.

    install_win10_x64.bat
	Main automated installation file to install the programs and 
	features to be used in the main WY_PROJ_BLENDER_EDITOR project
	which is in Windows 10 x64 compatible platform. 

    blender_setup.config
	Config XML file to hold the informations of the Blender module 
	files' existence in Python root directory.

    pydoc_iterator.bat
	Tkinter application tool which asks user to input the directory path
	to iterate the directory and finds the ".py" files and generate the
	Pydoc HTML pages in the same directory. 

    WY_PROJ_BLENDER_EDITOR/
	Main Blender editor project where customized exporters and 
	importers + OAuth tool sub projects exists.
    EXTRA
	External program installation and execution files and setup guide 
	to set up the development environment to run current project. 

    REVISION_HISTORY.txt	
	Main project revision history document.

    WY_PROJ_BLENDER_EDITOR.mpp
    	Main project plan document with Microsoft Project 2016.

    EXTRA
    	Collection of installation and executable files to install external
    	programs to set up current project running environment.

    shortcut - src
	Shortcut .lnk file links to main project source code folder.
    shortcut - PydocIterator
	Shortcut .lnk file links to the tool folder PydocIterator.
    shortcut - OAuthTimeReportDashboard
	Shortcut .lnk file links to the tool folder OAuthTimeReportDashboard.
    shortcut - OAuthTestGenerator
	Shortcut .lnk file links to the tool folder OAuthTestGenerator.
    shortcut - main
	Shortcut .lnk file links to the project main folder.

================================================================================
Resources & Credits:
================================================================================
    ============================================================================
    - Blender:
      Tutorial:
         http://cobertos.com/compiling-blender-as-a-python-module-for
         -windows-10-x64/ 
      Resources:
     	git://git.blender.org/blender.git
	https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc14 
    ============================================================================
    - MinGW64 must be installed:
	https://sourceforge.net/projects/mingw/files/latest/download
	(mingw-get-setup.exe)
	- Execute the downloaded .exe file --> Follow instructions.
        *****Important step*****:
		MinGW installation Manager 
		--> Select packages 
		--> Installation menu 
		--> Apply Changes
		--> Proceed
    ============================================================================
    - Git must be isntalled:
	https://git-for-windows.github.io/
	(Git-2.14.1-64-bit.exe)
	- Execute the downloaded .exe file --> Follow instructions.
	*****Important step*****:
		--> Git-2.14.1-64-bit.exe --> Next --> Next 
		--> Adjusting your PATH enviroment
		--> Make sure the "Use Git from the Windows Command Prompt" 
		    is checked
		--> Proceed.
    ============================================================================
    - SVN must be installed:
        https://sliksvn.com/download/
	(SlikSVN 1.9.7 64 bits Windows)
	- Execute the downloaded .msi file --> Follow instructions.
    ============================================================================
    - CMake must be installed:
	https://cmake.org/download/ 
	(cmake-3.9.4-win64-x64.msi)
	- Execute the .msi file --> Follow instructions.
	*****Important step*****:
		--> cmake-3.9.4-win64-x64.msi --> Next 
		--> Accept terms agreement --> Next
		--> Install Options
		--> Check "Add CMake to the system PATH for the current user"
		--> Proceed
    ============================================================================
    - Python 3 must be installed:
	https://www.python.org/downloads/release/python-362/
	(python-3.6.2-amd64.exe Windows x86-64 executable installer)
	- Execute the downloaded .exe file --> Follow instructions.
	*****Important step*****:
		--> python-3.6.2-amd64.exe
		--> Check "Add Python 3.6 to PATH" --> Install Now
	(If missed this step, it is ok, just execute the installation file 
 	 again --> Click "Modify" --> Next 
	       --> Check "Add Python to environment variables" --> Install)
    ============================================================================
    - Visual Studio 2017 must be installed:
	https://www.visualstudio.com/downloads/
	(Visual Studio Community 2017 version 15.2 Release)
	(Windows SDK Version: 10.0.15063.0)
    ============================================================================
