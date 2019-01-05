================================================================================  
                                    READ ME
================================================================================
Directory name: 
    - WY_PROJ_BLENDER_EDITOR\EXTRA.

================================================================================
Directory description:
================================================================================
cmake-3.9.4-win64-x64.msi
	CMake installation file.
	This is used to build the Blender source code and libraries 
	into bpy module in order to import Blender in standard Python.
Git-2.14.1-64-bit.exe
	Git installation file.
	This is to download Blender source code from 
	git://git.blender.org/blender.git
mingw-get-setup.exe
	MinGW installation file.
	This is to use makefile feature.
python-3.6.2-amd64.exe
	Python installation file.
Slik-Subversion-1.9.7-x64.msi
	SVN installation file.
	This is to download Blender libraries from 
	https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc14.
vs_community__1560776263.1499642898.exe
	Visual Studio 2017 installation file.
	This is to use "devenv" command to compile the Blender source code
	to create Blender Visual Studio project solution file to run with
	CMake to create bpy.pyd Blender module file to be imported to 
	main standard Python external modules folder.

blender-git/		
	Blender module folder where Blender source code and libraries are
	downloaded inside and generates the bpy.pyd module file and related 
	.dll files with CMake and Visual Studio devenv to be imported to the 
	standard Python external module by copying the generated Blender moudle 
	and dll files into the Python root directory's lib/site-packages folder
 	automatically which can be found by "where Python.exe" command. This 
	processes are done inside install.bat file all at once.

GUIDE_EXE.txt		
	Guide to generate main project set up executable setup.exe file 
	with ALZip self extractor.

GUIDE_INSTALL_BAT_ADMIN_SHORTCUT_TARGET.txt
	Guide to generate the main project install batch file shorcut to 
	run the main batch file in admin mode to access environment PATH 
	directly, and the directory path will change to "C:/Windows/System32" 
	automatically when run in admin mode, I needed few more step to 
	change the batch file run in admin directory before running.

================================================================================
Descriptions:
================================================================================
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
