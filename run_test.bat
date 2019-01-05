::==============================================================================
:: Main batch file which generates the test cases for the project and 
:: execute them for stablized codes
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-10-24
:: Last Updated: 2017-12-28
:: Desccription: 
::    This file contains the make file processs of the sub project inside the
::    main project called "OAuthTestGenerator" inside 
::    \WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\tools
::    \OAuthTestGenerator folder which generates the unit test 
::    cases using the data retrieved from private Google Spreadsheet and 
::    execute them inside the make call to make sure the code is stable.
::
:: Pre-condition:
::    0. install_win10_x64.bat is successfully ran.
::
:: Expected Result:
::     - Test cases for each member function inside each classes are
::       generated and organized into folders inside 
::       "WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\test" folder
::       which every folder contains the followings:
::           - Test case data text file.
::             (eg. WYCoordsysTestCaseData___init__.txt)
::           - Test case result output file.
::             (eg. WYCoordsysTestCaseResult___init__.txt)
::           - Independent makefile which does the same processes for each 
::             functions.
::             (eg. makefile_WYCoordsysTestCases___init__)
::           - HTML Pydoc document API page.
::             (eg. WYCoordsysTestCases___init__.html)
::           - Main unit test case file for current function.
::             (eg. WYCoordsysTestCases___init__.py)
::     - All the unit test case results for each functions will be 
::       appended into single result output file inside 
::       "WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\" folder.
::       (eg. WYCoordsysTestCaseResults.txt)
:: How to check:
::     - Check the unit test case result output of each class files
::       inside ""WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\" folder.
::       (eg. WYCoordsysTestCaseResults.txt)
:: Errors:
::     
::==============================================================================

@echo off

::==============================================================================
:: Set new line character start
set \n=^




:: Set new line character End
::==============================================================================

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Check Blender module is compiled and the built module is imported to 
:: Python root directory properly before running test cases.
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

echo CMake ... 
:: Build with CMake if not alreadt built
:: Indicate the version of Visual Studio to CMake with with
:: "Visual Studio 15 Win64" if Visual Studio version is higher than 2015
IF %built% EQU false (cmake -DWITH_PLAYER=OFF -DWITH_PYTHON_INSTALL=OFF^
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

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Run tests.
::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
::==============================================================================
:: Delete the test cases folder if exists
::==============================================================================
IF exist %cd%\WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\test\ (rmdir /S /Q %cd%\WY_PROJ_BLENDER_EDITOR\MESH_MAT_EXPORTER\src\test\) ELSE (echo "test" folder is not generated yet)

::==============================================================================
:: Run test case generator with makefile
::==============================================================================
cd .\WY_PROJ_BLENDER_EDITOR\MAIN\src\tools\OAuthTestGenerator && main.bat

::==============================================================================
:: Alert the user to show where the test cases results are located.
::==============================================================================
mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' );sh.Popup( 'Project unit test cases are generated inside ../WY_PROJ_BLENDER_EDITOR/MESH_MAT_EXPORTER/src/test folder.\nThe unit test cases results are generated inside ../WY_PROJ_BLENDER_EDITOR/MESH_MAT_EXPORTER/src folder.',0, 'Setup Error!', 64 );close()"

::==============================================================================
:: Ask for user input to decide whether to open the unit test case result 
:: containg folder in system file explorer
::==============================================================================
:: "y" - Execute the installation file.
:: "n" - Exit
:UserInputUnitTestCasesViewStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like open the unit test cases folder?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to open unit test cases folder.^^^%\n%%\n%^%\n%Enter "n" to cancel the process: %=%
If /I "%INPUT%"=="y" (start %cd%/../../../../../WY_PROJ_BLENDER_EDITOR/MESH_MAT_EXPORTER/src/test)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputUnitTestCasesViewEnd)^
       ELSE (GOTO UserInputUnitTestCasesViewStart))

:UserInputUnitTestCasesViewEnd

::==============================================================================
:: Ask for user input to decide whether to open the unit test case result 
:: containg folder in system file explorer
::==============================================================================
:: "y" - Execute the installation file.
:: "n" - Exit
:UserInputUnitTestCaseResultViewStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like open the unit test case result folder?(Y/N) ^^^%\n%%\n%^%\n%Enter "y" to open unit test case result folder.^^^%\n%%\n%^%\n%Enter "n" to cancel the process: %=%
If /I "%INPUT%"=="y" (start %cd%/../../../../../WY_PROJ_BLENDER_EDITOR/MESH_MAT_EXPORTER/src)^
 ELSE (IF /I "%INPUT%"=="n" (GOTO UserInputUnitTestCaseResultViewEnd)^
       ELSE (GOTO UserInputUnitTestCaseResultViewStart))

:UserInputUnitTestCaseResultViewEnd

