::==============================================================================
:: Main installation batch file to install the Blender module to the system 
:: Python root directory external module folder
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-19
:: Last Updated: 2017-12-28
:: Desccription: 
::    This file contains the installation processes of the Blender module 
::    - To generate the Pydoc HTML API pages with 
::      Blender source code inside, I needed to import the Blender as a
::      standard Python external module, so I downloaded the Blender 
::      source code and libraries to generate the bpy.pyd module to import
::      to the installed standard Python root directory Lib/site-packages
::      folder for external module import.
:: Pre-condition  :
::    0. setup_win64.bat must be ran.
::       Following programs will be installed for platform 
::       [ Windows 10 64 bits system ]
::    1. Git installed
::    2. SVN installed
::    3. Python 3.0 higher installed (+ pip)
::    4. CMake 3.9.4 installed
::    5. Visual Studio Community 2017 installed
:: Expected Result:
::     --> Check whether blender moudle is imported to Python root 
:: 	   directory or not. Set up blender-git if not imported.
:: 	   Skip to running test cases if imported.
::	   (Checks the file listed inside blender_setup.config)
::     --> Ask user to decide whether to fresh download or decompress the 
::	   blender-git using ZIP file.
::         (F) Fresh download blender-git.
::     		--> blender-git directory created to keep the Blender 
::		    moudle files.
::     		--> Blender source code downloaded from Git 
::	 	    (Cloned "blender")
::     		--> Libraries to built the Blender source code 
::		    into Windows 64 bits Python 3.0 compatible module 
::		    (Checkout "lib/win64_vc14")
::         (D) Decompress blender-git using existing ZIP file in EXTRA 
::	       folder.
::     		--> Decompress the blender-git.zip file inside EXTRA folder
::		    using PowerShell.
::     --> blender-git is setup at "../"
::     --> Go to "../blender-git"
::     --> build folder created
::     --> Building file into build folder generates INSTALL.vcxproj
::     --> Compile and run INSTALL.vcxproj with Visual Studio 2017
::     --> Generate bpy.pyd + .dll files + 2.79 folder.
::     --> Copy the Blender module resources to the main Python 
::         root directory's Lib/site-packages folder in the system.
::     --> Now the bpy is imported as standard Python external module
:: How to check:
::     --> Go the command line 
::     --> Type Python to start the interpreter
::     --> Type "import bpy"
::==============================================================================
@echo off
::==============================================================================
:: Set new line character start
set \n=^




:: Set new line character End
::==============================================================================

SET PROJ_ROOT=%cd%

::==============================================================================
:: Check Windows version
::==============================================================================
FOR /f "tokens=4-5 delims=. " %%i IN ('ver') DO SET VERSION=%%i.%%j
IF "%version%" == "10.0" echo Windows 10.0

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: MinGW64 install
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Sub installation batch file to install SVN to the system
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-16
:: Last Updated: 2017-10-26
:: Desccription: 
::    This file contains the installation processes of MinGW64.
:: Expected Result:
::     --> ../EXTRA/mingw-w64-install.exe executed 
::     --> Follow instruciton --> MinGW64 is installed 
::     --> PATH is refreshed --> Makefile working.
::==============================================================================
::==============================================================================
:: Check Makefile MinGW is installed in the system 
:: if not then alert the user to install it
::==============================================================================
:: Checks if MinGW exist, if not then asks  for the user input to decide to 
:: install the MinGW.
:: If user prompts character "y" then execute the .exe file in ./EXTRA folder
:: and proceed.
:: If user prompts character "n" then terminate the process.
:: If other character are prompted then let the user retype the input character.
SET mingw_install=

:: Get MinGW root directory with "where" command
FOR /f %%i in ('where make') DO SET mingw_root_dir=%%i

:: Alert messages for MinGW not exist, also provide the instruction to install it.
:: And terminate.
IF "%mingw_root_dir%" == "" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'MUST install MinGW!\nGo to ./EXTRA/mingw-get-setup.exe \n(OR Download "mingw-get-setup.exe" from "https://sourceforge.net/projects/mingw/files/latest/download") \n--> Execute the .exe file \n--> Follow instructions.\n\nDetail go to ./EXTRA/SETUP.txt',0, 'Setup Error!', 64 );close()"^
 && SET mingw_install=false)^
 ELSE (echo MinGW already installed ^
       && SET mingw_install=true)

IF %mingw_install%==false (GOTO UserInputMinGWInstallStart)^
 ELSE (GOTO UserInputMinGWInstallEnd)

::==============================================================================
:: Ask user to decide whether to install Git to the system using the 
:: installation file in ./EXTRA folder
::==============================================================================
:UserInputMinGWInstallStart
:: Ask for user input to decide whether to install MinGW or not
:: "y" - Execute the installation file.
:: "n" - Exit
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like install MinGW with ./EXTRA/mingw-get-setup.exe?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to proceed with installation.^^^%\n%%\n%^%\n%Enter "n" to cancel the process and terminate: %=%
If /I "%INPUT%"=="y" (start /WAIT /d ".\EXTRA" mingw-get-setup.exe)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputMinGWInstallExit)^
       ELSE (GOTO UserInputMinGWInstallStart))

:: Need to change the make.exe name in order to use the make command
copy c:\MinGW\bin\mingw32-make.exe c:\MinGW\bin\make.exe

GOTO UserInputMinGWInstallEnd
:UserInputMinGWInstallExit
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Terminating process ...',0, 'Setup Error!', 64 );close()"
exit
:UserInputMinGWInstallEnd

:: Add MinGW to environment PATH varaible by appending default location path
:: "C:\mingw64\bin\"
SETX PATH "%PATH%;C:\MinGW\bin" /M

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: SVN install
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Sub installation batch file to install SVN to the system
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-19
:: Last Updated: 2017-10-22
:: Desccription: 
::    This file contains the installation processes of Slik-Subversion-1.9.7.
:: Expected Result:
::     --> ../EXTRA/Slik-Subversion-1.9.7-x64.msi executed 
::     --> Follow instruciton --> SVN is installed 
::     --> PATH is refreshed --> SVN working.
::==============================================================================
::==============================================================================
:: Check SVN is installed in the system if not then alert the user to install it
::==============================================================================
:: Checks if SVN exist, if not then asks  for the user input to decide to 
:: install the SVN. 
:: If user prompts character "y" then execute the .exe file in ./EXTRA folder
:: and proceed.
:: If user prompts character "n" then terminate the process.
:: If other character are prompted then let the user retype the input character.
SET svn_install=

:: Get SVN root directory with "where" command
FOR /f %%i in ('where svn.exe') DO SET svn_root_dir=%%i

:: Alert messages for SVN not exist, also provide the instruction to install it.
:: And terminate.
IF "%svn_root_dir%" == "" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'MUST install SVN!\nGo to ./EXTRA/Slik-Subversion-1.9.7-x64.msi \n(OR Download "Slik-Subversion-1.9.7-x64.msi" from "https://sliksvn.com/download/" and extract the zip file) \n--> Execute the .msi file \n--> Follow instructions.\n\nDetail go to ./EXTRA/SETUP.txt',0, 'Setup Error!', 64 );close()"^
 && SET svn_install=false)^
 ELSE (echo SVN already installed ^
       && SET svn_install=true)

IF %svn_install%==false (GOTO UserInputSVNInstallStart)^
 ELSE (GOTO UserInputSVNInstallEnd)

::==============================================================================
:: Ask user to decide whether to install Git to the system using the 
:: installation file in ./EXTRA folder
::==============================================================================
:UserInputSVNInstallStart
:: Ask for user input to decide whether to install SVN or not
:: "y" - Execute the installation file.
:: "n" - Exit
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like install SVN with ./EXTRA/Slik-Subversion-1.9.7-x64.msi?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to proceed with installation.^^^%\n%%\n%^%\n%Enter "n" to cancel the process and terminate: %=%
If /I "%INPUT%"=="y" (start /WAIT /d ".\EXTRA" Slik-Subversion-1.9.7-x64.msi)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputSVNInstallExit)^
       ELSE (GOTO UserInputSVNInstallStart))
GOTO UserInputSVNInstallEnd
:UserInputSVNInstallExit
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Terminating process ...',0, 'Setup Error!', 64 );close()"
exit
:UserInputSVNInstallEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Git install
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Sub installation batch file to install Git to the system
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-19
:: Last Updated: 2017-10-22
:: Desccription: 
::    This file contains the installation processes of Git.
:: Expected Result:
::    --> ../EXTRA/Git-2.14.1-64-bit.exe executed 
::    --> Follow instruciton 
::    --> Git is installed --> PATH is refreshed --> Git working.
::==============================================================================

::==============================================================================
:: Check Git is installed in the system if not then alert the user to install it
::==============================================================================
:: Checks if Git exist, if not then asks  for the user input to decide to 
:: install the Git. 
:: If user prompts character "y" then execute the .exe file in ./EXTRA folder
:: and proceed.
:: If user prompts character "n" then terminate the process.
:: If other character are prompted then let the user retype the input character.
::==============================================================================
SET git_install=

:: Get Git root directory with "where" command
FOR /f %%i in ('where git.exe') DO SET git_root_dir=%%i

:: Alert messages for Git not exist, also provide the instruction to install it.
:: And terminate.
IF "%git_root_dir%" == "" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'MUST install Git!\nGo to ./EXTRA/Git-2.14.1-64-bit.exe \n(OR Download "Git-2.14.1-64-bit.exe" from "https://git-for-windows.github.io/") \n--> Execute the .exe file \n--> Follow instructions.\n\nDetail go to ./EXTRA/SETUP.txt',0, 'Setup Error!', 64 );close()"^
 && SET git_install=false)^
 ELSE (echo CMake installed^
       && SET git_install=true)

IF %git_install%==false (GOTO UserInputGitInstallStart)^
 ELSE (GOTO UserInputGitInstallEnd)

::==============================================================================
:: Ask user to decide whether to install Git to the system using the 
:: installation file in ./EXTRA folder
::==============================================================================
:UserInputGitInstallStart
:: Ask for user input to decide whether to install Git or not
:: "y" - Execute the installation file.
:: "n" - Exit
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like install Git with ./EXTRA/Git-2.14.1-64-bit.exe?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to proceed with installation.^^^%\n%%\n%^%\n%Enter "n" to cancel the process and terminate: %=%
If /I "%INPUT%"=="y" (start /WAIT /d ".\EXTRA" Git-2.14.1-64-bit.exe)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputGitInstallExit)^
       ELSE (GOTO UserInputGitInstallStart))
GOTO UserInputGitInstallEnd
:UserInputGitInstallExit
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Terminating process ...',0, 'Setup Error!', 64 );close()"
exit
:UserInputGitInstallEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Python install
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Sub installation batch file to install Python 3.0 to the system
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-19
:: Last Updated: 2017-10-22
:: Desccription: 
::    This file contains the installation processes of Python 3.0.
:: Expected Result:
::     --> ../EXTRA/python-3.6.2-amd64.exe executed 
::     --> Follow instruciton --> Python is installed 
::     --> PATH is refreshed --> Python working.
::==============================================================================
::==============================================================================
:: Check Python is installed in the system if not then alert the user to install
::==============================================================================
:: Checks if Python exist, if not then asks  for the user input to decide to 
:: install the Python.
:: If user prompts character "y" then execute the .exe file in ./EXTRA folder
:: and proceed.
:: If user prompts character "n" then terminate the process.
:: If other character are prompted then let the user retype the input character.
SET python_install=

:: Get Python root directory with "where" command
FOR /f %%i in ('where python.exe') DO SET python_root_dir=%%i

:: Alert messages for Python not exist, also provide the instruction to install it.
:: And terminate.
IF "%python_root_dir%" == "" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'MUST install Python!\nGo to ./EXTRA/python-3.6.2-amd64.exe (OR \nDownload "python-3.6.2-amd64.exe" from "https://www.python.org/downloads/release/python-362/") \n--> Execute the .exe file to install Python to the system.\n\nDetail go to ./EXTRA/SETUP.txt',0, 'Setup Error!', 64 );close()"^
 && SET python_install=false)^
 ELSE (echo Python already installed^
       && SET python_install=true)

IF %python_install%==false (GOTO UserInputPythonInstallStart)^
 ELSE (GOTO UserInputPythonInstallEnd)

::==============================================================================
:: Ask user to decide whether to install Git to the system using the 
:: installation file in ./EXTRA folder
::==============================================================================
:UserInputPythonInstallStart
:: Ask for user input to decide whether to install Python or not
:: "y" - Execute the installation file.
:: "n" - Exit
SET INPUT=

SET /P INPUT=^^^%\n%%\n%^%\n%Would you like install Python with ./EXTRA/python-3.6.2-amd64.exe?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to proceed with installation.^^^%\n%%\n%^%\n%Enter "n" to cancel the process and terminate: %=%
If /I "%INPUT%"=="y" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Remember to add the system environment PATH when installing Python!!!',0, 'Setup Error!', 64 );close()"^
 && start /WAIT /d ".\EXTRA" python-3.6.2-amd64.exe)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputPythonInstallExit)^
       ELSE (GOTO UserInputPythonInstallStart))
GOTO UserInputPythonInstallEnd
:UserInputPythonInstallExit
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Terminating process ...',0, 'Setup Error!', 64 );close()"
exit
:UserInputPythonInstallEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: CMake install
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Sub installation batch file to install CMake 3.9.4 to the system
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-19
:: Last Updated: 2017-10-19
:: Desccription: 
::    This file contains the installation processes of CMake 3.9.4.
:: Expected Result:
::     ../EXTRA/cmake-3.9.4-win64-x64.msi executed --> Follow instruciton -->
::     CMake is installed --> PATH is refreshed --> CMake working.
::==============================================================================

::==============================================================================
:: Check CMake is installed in the system if not then alert the user to install
::==============================================================================
:: Checks if CMake exist, if not then asks  for the user input to decide to 
:: install the CMake.
:: If user prompts character "y" then execute the .msi file in ./EXTRA folder
:: and proceed.
:: If user prompts character "n" then terminate the process.
:: If other character are prompted then let the user retype the input character.
SET cmake_install=

:: Get CMake root directory with "where" command
FOR /f %%i in ('where cmake.exe') DO SET cmake_root_dir=%%i

:: Alert messages for CMake not exist, also provide the instruction to install it.
:: And terminate.
IF "%cmake_root_dir%" == "" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'MUST install CMake!\nGo to ./EXTRA/cmake-3.9.3-win64-x64.msi \n(OR Download "cmake-3.9.3-win64-x64.msi" from "https://cmake.org/download/") \n--> Execute the .msi file to install CMake to the system\n\nDetail go to ./EXTRA/SETUP.txt',0, 'Setup Error!', 64 );close()"^
 && SET cmake_install=false)^
 ELSE (echo CMake already installed^
       && SET cmake_install=true)

IF %cmake_install%==false (GOTO UserInputCMakeInstallStart) ELSE (GOTO UserInputCMakeInstallEnd)

::==============================================================================
:: Ask user to decide whether to install Git to the system using the 
:: installation file in ./EXTRA folder
::==============================================================================
:UserInputCMakeInstallStart
:: Ask for user input to decide whether to install CMake or not
:: "y" - Execute the installation file.
:: "n" - Exit
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like install CMake with ./EXTRA/cmake-3.9.4-win64-x64.msi?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to proceed with installation.^^^%\n%%\n%^%\n%Enter "n" to cancel the process and terminate: %=%
If /I "%INPUT%"=="y" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Remember to add the system environment PATH when installing CMake!!!',0, 'Setup Error!', 64 );close()"^
 && start /WAIT /d ".\EXTRA" cmake-3.9.4-win64-x64.msi)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputCMakeInstallExit)^
      ELSE (GOTO UserInputCMakeInstallStart))
GOTO UserInputCMakeInstallEnd
:UserInputCMakeInstallExit
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Terminating process ...',0, 'Setup Error!', 64 );close()"
exit
:UserInputCMakeInstallEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Visual Studio 2017 install
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Sub installation batch file to install Visual Studio 2017 to the system
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-19
:: Last Updated: 2017-10-19
:: Desccription: 
::    This file contains the installation processes of Visual Studio 
::    Community 2017.
:: Expected Result:
::     --> ../EXTRA/vs_community__1560776263.1499642898.exe executed 
::     --> Follow instruciton -->
::     --> Visual Studo Commnuity 2017 installed
::     --> C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\
::            Common7\IDE\devenv.exe installed
::     --> devenv working.
::==============================================================================

::==============================================================================
:: Check Visual Studio Community 2017 is installed in the system 
:: if not then alert the user to install it
::==============================================================================
:: Checks if Visual Studio 2017 exist, if not then asks for the user input to 
:: decide to install the Visual Studio 2017.
:: If user prompts character "y" then execute the .exe file in ./EXTRA folder
:: and proceed.
:: If user prompts character "n" then terminate the process.
:: If other character are prompted then let the user retype the input character.
IF not exist "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'MUST install Visual Studio 2017!\nGo to ./EXTRA/vs_community__1560776263.1499642898.exe \n(OR Download "vs_community__1560776263.1499642898.exe" from "https://www.visualstudio.com/downloads/") \n--> Execute the .exe file \n--> Follow instructions.\n\nDetail go to ./EXTRA/SETUP.txt',0, 'Setup Error!', 64 );close()"^
 && SET vs2017_install=false)^
 ELSE (echo Visual Studio 2017 already installed^
 && SET vs2017_install=true)


IF %vs2017_install%==false (GOTO UserInputVS2017InstallStart)^
 ELSE (GOTO UserInputVS2017InstallEnd)

::==============================================================================
:: Ask user to decide whether to install Git to the system using the 
:: installation file in ./EXTRA folder
::==============================================================================
:UserInputVS2017InstallStart
:: Ask for user input to decide whether to install Visual Studio 2017 or not
:: "y" - Execute the installation file.
:: "n" - Exit
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like install VS2017 with ./EXTRA/vs_community__1560776263.1499642898.exe?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to proceed with installation.^^^%\n%%\n%^%\n%Enter "n" to cancel the process and terminate: %=%
If /I "%INPUT%"=="y" (start /WAIT /d ".\EXTRA" vs_community__1560776263.1499642898.exe)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputVS2017InstallExit)^
       ELSE (GOTO UserInputVS2017InstallStart))
GOTO UserInputVS2017InstallEnd
:UserInputVS2017InstallExit
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Terminating process ...',0, 'Setup Error!', 64 );close()"
exit
:UserInputVS2017InstallEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Refresh environment variable PATH
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
SET org=%PATH%
for /f "tokens=3*" %%A in ('REG QUERY "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path') DO (SET syspath=%%A %%B)
for /f "tokens=3*" %%A in ('reg query "HKCU\Environment" /v Path') DO (SET userpath=%%A)
SET PATH=%org%;%syspath%;%userpath%


::==============================================================================
:: Double check if the necessary programs are installed in the system for 
:: further proceeding
::==============================================================================
SET mingw_root_dir=
SET svn_root_dir=
SET git_root_dir=
SET python_root_dir=
SET cmake_root_dir=
FOR /f %%i in ('where make.exe')   DO SET mingw_root_dir=%%i
FOR /f %%i in ('where svn.exe')    DO SET svn_root_dir=%%i
FOR /f %%i in ('where git.exe')    DO SET git_root_dir=%%i
FOR /f %%i in ('where python.exe') DO SET python_root_dir=%%i
FOR /f %%i in ('where cmake.exe')  DO SET cmake_root_dir=%%i

IF "%mingw_root_dir%"    == "" (GOTO Reinstall)
IF "%svn_root_dir%"      == "" (GOTO Reinstall)
IF "%git_root_dir%"      == "" (GOTO Reinstall)
IF "%python_root_dir%"   == "" (GOTO Reinstall)
IF "%cmake_root_dir%"    == "" (GOTO Reinstall)
IF not exist "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe" (GOTO Reinstall)

:: If all the installation is successful then go to proceed line
GOTO Proceed

:Reinstall

:: Wait for user to install the necessary programs
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Run setup_win64.bat to install mandatory programs first!!! Terminating...',0, 'Setup Error!', 64 );close()"
:: Terminate current process
exit

:Proceed

::==============================================================================
:: Install Google API Python client to access the Google Spreadsheet through
:: Python scripts
::==============================================================================
pip install --upgrade google-api-python-client


::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Blender install + import module
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Get Blender external module Python check file and folder paths.
:: Checking if these files exists using relative paths appended onto the 
:: Python root directory:
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\2.79
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\bpy.pyd
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\OpenColorIO.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\OpenAL32.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\avcodec-57.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\avdevice-57.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\avformat-57.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\avutil-55.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\BlendThumb64.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\pthreadVC2.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\python36.dllSDL2.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\swresample-2.dll
::     C:\Users\Nickj\AppData\Local\Programs\Python\Python36\python.exe\..\Lib\site-packages\swscale-4.dll
::==============================================================================
:: Get Python root directory with "where" command
FOR /f %%i in ('where python.exe') DO SET python_root_dir=%%i

SET blender_2_79=%python_root_dir%\..\2.79
SET bool_blender_2_79=false

SET blender_bpy=%python_root_dir%\..\Lib\site-packages\bpy.pyd
SET bool_blender_bpy=false

SET blender_opencolorio=%python_root_dir%\..\Lib\site-packages\OpenColorIO.dll
SET bool_blender_opencolorio=false

SET blender_openal32=%python_root_dir%\..\Lib\site-packages\OpenAL32.dll
SET bool_blender_openal32=false

SET blender_avcodec=%python_root_dir%\..\Lib\site-packages\avcodec-57.dll
SET bool_blender_avcodec=false

SET blender_avdevice=%python_root_dir%\..\Lib\site-packages\avdevice-57.dll
SET bool_blender_avdevice=false

SET blender_avformat=%python_root_dir%\..\Lib\site-packages\avformat-57.dll
SET bool_blender_avformat=false

SET blender_avutil=%python_root_dir%\..\Lib\site-packages\avutil-55.dll
SET bool_blender_avutil=false

SET blender_blendthumb64=%python_root_dir%\..\Lib\site-packages\BlendThumb64.dll
SET bool_blender_blendthumb64=false

SET blender_pthreadvc2=%python_root_dir%\..\Lib\site-packages\pthreadVC2.dll
SET bool_blender_pthreadvc2=false

SET blender_python36=%python_root_dir%\..\Lib\site-packages\python36.dll
SET bool_blender_python36=false

SET blender_sdl2=%python_root_dir%\..\Lib\site-packages\SDL2.dll
SET bool_blender_sdl2=false

SET blender_swresample2=%python_root_dir%\..\Lib\site-packages\swresample-2.dll
SET bool_blender_swresample2=false

SET blender_swscale4=%python_root_dir%\..\Lib\site-packages\swscale-4.dll
SET bool_blender_swscale4=false

::==============================================================================
:: Read the XML config file to check whether the files are imported properly
:: Set the variables values according to the data read from the XML file.
::==============================================================================
for /F tokens^=2^,3^,5delims^=^<^"^= %%a in (blender_setup.config) do (IF "%%a" equ "name" (^
IF "%%b" == "2.79" (echo %%b %%c) ELSE (^
IF "%%b" == "bpy.pyd" (echo %%b %%c) ELSE (^
IF "%%b" == "OpenColorIO.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "OpenAL32.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "avcodec-57.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "avdevice-57.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "avformat-57.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "avutil-55.dll" (echo %%b %%) ELSE (^
IF "%%b" == "BlendThumb64.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "pthreadVC2.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "SDL2.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "swresample-2.dll" (echo %%b %%c) ELSE (^
IF "%%b" == "swscale-4.dll" (echo %%b %%c)))))))))))))))

::==============================================================================
:: Check file exist if not got :BlenderSetupStart to start re-setup Blender
:: module import
::==============================================================================
IF exist "%blender_2_79%" ( SET bool_blender_2_79=true && echo 2.79 exists )^
 ELSE ( SET bool_blender_2_79=false && echo 2.79 not exist && GOTO BlenderSetupStart )

IF exist "%blender_bpy%" ( SET bool_blender_bpy=true && echo bpy.pyd exists )^
 ELSE ( SET bool_blender_bpy=false && echo bpy.pyd not exist && GOTO BlenderSetupStart )

IF exist "%blender_opencolorio%" ( SET bool_blender_opencolorio=true && echo OpenColorIO.dll exists )^
 ELSE ( SET bool_blender_opencolorio=false &&echo OpenColorIO.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_openal32%" ( SET bool_blender_openal32=true && echo OpenAL32.dll exists )^
 ELSE ( SET bool_blender_openal32=false && echo OpenAL32.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_avcodec%" ( SET bool_blender_avcodec=true && echo avcodec-57.dll exists )^
 ELSE ( SET bool_blender_avcodec=false && echo avcodec-57.dll not exist && GOTO BlenderSetupStart )
 
IF exist "%blender_avdevice%" ( SET bool_blender_avdevice=true && echo avdevice-57.dll exists )^
 ELSE ( SET bool_blender_avdevice=false && echo avdevice-57.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_avformat%" ( SET bool_blender_avformat=true && echo avformat-57.dll exists )^
 ELSE ( SET bool_blender_avformat=false && echo avformat-57.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_avutil%" ( SET bool_blender_avutil=true && echo avutil-55.dll exists )^
 ELSE ( SET bool_blender_avutil=false && echo avutil-55.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_blendthumb64%" ( SET bool_blender_blendthumb64=true && echo BlendThumb64.dll exists )^
 ELSE ( SET bool_blender_blendthumb64=false && echo BlendThumb64.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_pthreadvc2%" ( SET bool_blender_pthreadvc2=true && echo pthreadVC2.dll exists )^
 ELSE ( SET bool_blender_pthreadvc2=false && echo pthreadVC2.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_python36%" ( SET bool_blender_python36=true && echo python36.dll exists )^
 ELSE ( SET bool_blender_python36=false && echo python36.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_sdl2%" ( SET bool_blender_sdl12=true && echo SDL2.dll exists )^
 ELSE ( SET bool_blender_sdl12=false && echo SDL2.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_swresample2%" ( SET bool_blender_swresample2=true && echo swresample-2.dll exists )^
 ELSE ( SET bool_blender_swresample2=false && echo swresample-2.dll not exist && GOTO BlenderSetupStart )

IF exist "%blender_swscale4%" ( SET bool_blender_swscale4=true && echo swscale-4.dll exists )^
 ELSE ( SET bool_blender_swscale4=false && echo swscale-4.dll not exist && GOTO BlenderSetupStart )

::==============================================================================
:: Write the XML config file to store the file existence value to decide
:: whether to re-setup the project.
::==============================================================================
( 
echo(^<?xml version="1.0"?^>
echo(^<configuration^>
echo(   ^<WY_PROJ_BLENDER_EDITOR^>
echo(      ^<Blender setup^>
echo(            ^<name="2.79" value="%bool_blender_2_79%" description="folder"/^>
echo(            ^<name="bpy.pyd" value="%bool_blender_opencolorio%" description="file"/^>
echo(            ^<name="OpenColorIO.dll" value="%bool_blender_opencolorio%" description="file"/^>
echo(            ^<name="OpenAL32.dll" value="%bool_blender_openal32%" description="file"/^>
echo(            ^<name="avcodec-57.dll" value="%bool_blender_avcodec%" description="file"/^>
echo(            ^<name="avdevice-57.dll" value="%bool_blender_avdevice%" description="file"/^>
echo(            ^<name="avformat-57.dll" value="%bool_blender_avformat%" description="folder"/^>
echo(            ^<name="avutil-55.dll" value="%bool_blender_avutil%" description="file"/^>
echo(            ^<name="BlendThumb64.dll" value="%bool_blender_blendthumb64%" description="file"/^>
echo(            ^<name="pthreadVC2.dll" value="%bool_blender_pthreadvc2%" description="file"/^>
echo(            ^<name="python36.dll" value="%bool_blender_python36%" description="file"/^>
echo(            ^<name="SDL2.dll" value="%bool_blender_sdl2%" description="file"/^>
echo(            ^<name="swresample-2.dll" value="%bool_blender_swresample2%" description="file"/^>
echo(            ^<name="swscale-4.dll" value="%bool_blender_swscale4%" description="file"/^>
echo(      ^</Blender setup^>
echo(   ^</WY_PROJ_BLENDER_EDITOR^>
echo(^</configuration^>
)> blender_setup.config

GOTO BlenderSetupEnd

:BlenderSetupStart

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: blender-git user input option:
:: "y" - Fresh download.
:: "n" - Decompress from ZIP file inside EXTRA folder.
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Ask for user input to decide whether to decompress ZIP for blender-git folder
:: or do the fresh download.
::==============================================================================
cd %PROJ_ROOT%
:UserInputBlenderGitOptionStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to: Fresh download blender-git(F) OR Decompress from existing ZIP file?(D) ^^^%\n%%\n%^%\n%Enter "F" to fresh download.^^^%\n%%\n%^%\n%Enter "D" to decompress from existing ZIP file: %=%
If /I "%INPUT%"=="f" (GOTO UserInputBlenderGitOptionFreshDownloadStart)^
 ELSE (IF /I "%INPUT%"=="d" (GOTO UserInputBlenderGitOptionDecompressStart)^
       ELSE (GOTO UserInputBlenderGitOptionStart))

:UserInputBlenderGitOptionFreshDownloadStart

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: blender-git fresh download
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
echo Fresh downloading blender-git ...
::==============================================================================
:: Check if the Blender source directory exist
::==============================================================================
IF exist "..\blender-git" ( echo "..\blender-git" exists )^
 ELSE ( mkdir "..\blender-git" && echo "..\blender-git" created)
::==============================================================================
:: Go to "blender-git" directory
::==============================================================================
CD %cd%\..\blender-git
::==============================================================================
:: Setup Blender as an external Python module
::==============================================================================
:: Download the Blender source directory from Git
git clone git://git.blender.org/blender.git
:: Directory "blender" will be generated with Blender source code inside
CD blender
git submodule update --init --recursive
:: Naviage back to main project folder
CD ..

:: Download pre-compiled Blender libraries by checking out with SVN 
:: This will generate the folder "lib/win64_vc14" which contains the libraries
:: to generate the Windows 10 64 bits compatible and Visual Studio 2017 
:: compilable Blender module.
:: ******Need to checkout "zlib" folder independetly because for some reason, 
:: the above command have error such that "zlib" is not downloaded which 
:: causes error when bpy module is imported
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc14/zlib/ lib/win64_vc14/zlib/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc14       lib/win64_vc14      
::==============================================================================
echo Fresh download blender-git complete ...

GOTO UserInputBlenderGitOptionDecompressEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: blender-git decompress from ZIP inside EXTRA folder
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:UserInputBlenderGitOptionDecompressStart
echo Decompressing blender-git ...
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem';[IO.Compression.ZipFile]::ExtractToDirectory('./EXTRA/blender-git.zip', '../'); }"
echo Decompress blender-git complete ...

::==============================================================================
:: Go to "blender-git" directory
::==============================================================================
CD %cd%\..\blender-git

:UserInputBlenderGitOptionDecompressEnd

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Build with CMake
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

echo building ... 
:: Create a build folder to keep the executable files to generate the Blender 
:: module
IF exist "build" (echo "build" exists) ELSE (mkdir build)

:: Go inside the build folder to CMake the Blender source code with libraries 
:: to generate the Windows 10 64 bits compatible and Visual Studio 2017 
:: compilable Blender module.
CD build

:: Check if the CMake is already completed
IF exist "INSTALL.vcxproj" (set built=true) ELSE (set built=false)
echo %built%


:: Build with CMake if not alreadt built
:: Indicate the version of Visual Studio to CMake with with
:: "Visual Studio 15 Win64" if Visual Studio version is higher than 2015
IF %built% EQU false (echo CMaking may take around 15 minutes ...  && cmake -DWITH_PLAYER=OFF -DWITH_PYTHON_INSTALL=OFF^
 -DWITH_PYTHON_MODULE=ON^
 -DPYTHON_VERSION=3.6^
 -G"Visual Studio 15 Win64" ../blender) else (echo CMake not needed)

::==============================================================================
:: Check if "bin" folder is generated inside "build" folder to check 
:: the CMake result the reuslting generated Blender module will be located 
:: inside "build\bin\Release" folder if not then run with Visual Studio 2017 
::==============================================================================
::IF exist "bin" (echo "Run with Visual Studio 2017 success!!!")^
:: ELSE (echo Visual Studio building bpy.pyd and other modules may take around 15 minutes ... &&  "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe" Blender.sln /build Release /Project INSTALL)

"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe" Blender.sln /build Release /Project INSTALL
::==============================================================================
:: Copy all the generated Blender module 2.79 folder, .dll files and bpy.pyd 
:: module file to the Python root directory's "Lib\site-packages" folder to 
:: import bpy as standard Python module
:: It might ask us to overwrite the file or not then 
::    type "y" to overwrite for a file
::    type "n" to not overwrite for a file
::    type "a" to overwrite all
::==============================================================================
:: Get Python root directory with "where" command
FOR /f %%i in ('where python.exe') DO SET python_root_dir=%%i
IF %python_root_dir%=="" (mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Cannot find Python root directory!!!',0, 'Setup Error!', 64 );close()" && GOTO CopyBlenderModuleExit) ELSE (GOTO CopyBlenderModuleStart)

echo Copying files to Python root directory ... 

:: Move the generated Blender module and .dll files to the Python root 
:: directory found in the system
:CopyBlenderModuleStart
copy bin\Release\bpy.pyd %python_root_dir%\..\Lib\site-packages
copy bin\Release\*.dll %python_root_dir%\..\Lib\site-packages
xcopy /E bin\Release\2.79 %python_root_dir%\..\2.79\

:CopyBlenderModuleExit

:BlenderSetupEnd

::==============================================================================
:: Type "import bpy" in Python interpretor or then terminate the interpretor 
:: to see whether there are any errors occur importing Blender module "bpy.pyd"
::==============================================================================
echo Blender external module is successfully imported to Python!!!

::==============================================================================
:: Execute the test cases for this project before using.
::==============================================================================
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Project setup complete!!! Click OK to proceed on running test cases ...',0, 'Setup Error!', 64 );close()"

::==============================================================================
:: Ask for user input to decide whether to execute the run_test.bat
:: containg folder in system file explorer
::==============================================================================
:: "y" - Execute the installation file.
:: "n" - Exit
cd %PROJ_ROOT%
:UserInputRunTestBatStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like generate and run the unit test cases for current project?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to run.^^^%\n%%\n%^%\n%Enter "n" to cancel the process: %=%
If /I "%INPUT%"=="y" (run_test.bat)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputRunTestBatEnd)^
       ELSE (GOTO UserInputRunTestBatStart))

:UserInputRunTestBatEnd

