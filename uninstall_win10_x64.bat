::==============================================================================
:: Main uninstallation batch file to uninstall the Blender module to the system 
:: Python root directory external module folder and related installed programs.
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-12-28
:: Last Updated: 2017-12-28
:: Desccription: 
::    This file contains the uninstallation processes of the Blender module 
::    - 
::==============================================================================
@echo off
::==============================================================================
:: Set new line character start
set \n=^




:: Set new line character End
::==============================================================================

SET PROJ_ROOT=%cd%

::==============================================================================
:: Uninstall Blender moudle in Python root directory
::==============================================================================
:UserInputBlenderModuleUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall Blender module? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (GOTO UserInputBlenderModuleUninstall)^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputBlenderModuleUninstallEnd)^
    ELSE (GOTO UserInputBlenderModuleUninstallStart))

:UserInputBlenderModuleUninstall

::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:: Blender module uninstall
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
SET blender_bpy=%python_root_dir%\..\Lib\site-packages\bpy.pyd
SET blender_opencolorio=%python_root_dir%\..\Lib\site-packages\OpenColorIO.dll
SET blender_openal32=%python_root_dir%\..\Lib\site-packages\OpenAL32.dll
SET blender_avcodec=%python_root_dir%\..\Lib\site-packages\avcodec-57.dll
SET blender_avdevice=%python_root_dir%\..\Lib\site-packages\avdevice-57.dll
SET blender_avformat=%python_root_dir%\..\Lib\site-packages\avformat-57.dll
SET blender_avutil=%python_root_dir%\..\Lib\site-packages\avutil-55.dll
SET blender_blendthumb64=%python_root_dir%\..\Lib\site-packages\BlendThumb64.dll
SET blender_pthreadvc2=%python_root_dir%\..\Lib\site-packages\pthreadVC2.dll
SET blender_python36=%python_root_dir%\..\Lib\site-packages\python36.dll
SET blender_sdl2=%python_root_dir%\..\Lib\site-packages\SDL2.dll
SET blender_swresample2=%python_root_dir%\..\Lib\site-packages\swresample-2.dll
SET blender_swscale4=%python_root_dir%\..\Lib\site-packages\swscale-4.dll

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
:: Delete all the files that is imported through the installer
::==============================================================================
echo Uninstalling "%blender_2_79%" ...
IF exist "%blender_2_79%" ( rmdir /S /Q %blender_2_79%)

echo Uninstalling "%blender_bpy%" ...
IF exist "%blender_bpy%" ( DEL /F %blender_bpy% )

echo Uninstalling "%blender_opencolorio%" ...
IF exist "%blender_opencolorio%" ( DEL /F %blender_opencolorio% )

echo Uninstalling "%blender_openal32%" ...
IF exist "%blender_openal32%" ( DEL /F %blender_openal32% )

echo Uninstalling "%blender_avcodec%" ...
IF exist "%blender_avcodec%" ( DEL /F %blender_avcodec% )

echo Uninstalling "%blender_avdevice%" ...
IF exist "%blender_avdevice%" ( DEL /F %blender_avdevice% )

echo Uninstalling "%blender_avformat%" ...
IF exist "%blender_avformat%" ( DEL /F %blender_avformat% )

echo Uninstalling "%blender_avutil%" ...
IF exist "%blender_avutil%" ( DEL /F %blender_avutil% )

echo Uninstalling "%blender_blendthumb64%" ...
IF exist "%blender_blendthumb64%" ( DEL /F %blender_blendthumb64% )

echo Uninstalling "%blender_pthreadvc2%" ...
IF exist "%blender_pthreadvc2%" ( DEL /F %blender_pthreadvc2% )

echo Uninstalling "%blender_python36%" ...
IF exist "%blender_python36%" ( DEL /F %blender_python36% )

echo Uninstalling "%blender_sdl2%" ...
IF exist "%blender_sdl2%" ( DEL /F %blender_sdl2% )

echo Uninstalling "%blender_swresample2%" ...
IF exist "%blender_swresample2%" ( DEL /F %blender_swresample2% )

echo Uninstalling "%blender_swscale4%" ...
IF exist "%blender_swscale4%" ( DEL /F %blender_swscale4% )

:UserInputBlenderModuleUninstallEnd

::==============================================================================
:: Uninstall programs which are probably installed by the installer.
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

SET bool_vs_exist=
IF exist "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe" (SET bool_vs_exist=true)


::==============================================================================
:: Uninstall MinGW
::==============================================================================
:UserInputMinGWUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall MinGW? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (^
    IF NOT "%mingw_root_dir%" == "" (rmdir /S /Q  C:\mingw64\)^
    ELSE (GOTO UserInputMinGWUninstallEnd))^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputMinGWUninstallEnd)^
    ELSE (GOTO UserInputMinGWUninstallStart))
:UserInputMinGWUninstallEnd

::==============================================================================
:: Uninstall SlikSVN
::==============================================================================
:UserInputSlikSVNUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall SlikSVN? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (^
    IF NOT "%svn_root_dir%" == "" (start /WAIT /d ".\EXTRA" Slik-Subversion-1.9.7-x64.msi)^
    ELSE (GOTO UserInputSlikSVNUninstallEnd))^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputSlikSVNUninstallEnd)^
    ELSE (GOTO UserInputSlikSVNUninstallStart))
:UserInputSlikSVNUninstallEnd

::==============================================================================
:: Uninstall Git
::==============================================================================
:UserInputGitUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall Git? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (^
    IF NOT "%git_root_dir%" == "" (start /WAIT /d "C:\Program Files\Git\" unins000.exe)^
    ELSE (GOTO UserInputGitUninstallEnd))^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputGitUninstallEnd)^
    ELSE (GOTO UserInputGitUninstallStart))
:UserInputGitUninstallEnd


::==============================================================================
:: Uninstall Python
::==============================================================================
:UserInputPythonUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall Python? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (^
    IF NOT "%python_root_dir%" == "" (start /WAIT /d ".\EXTRA" python-3.6.2-amd64.exe)^
    ELSE (GOTO UserInputPythonUninstallEnd))^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputPythonUninstallEnd)^
    ELSE (GOTO UserInputPythonUninstallStart))
:UserInputPythonUninstallEnd


::==============================================================================
:: Uninstall CMake
::==============================================================================
:UserInputCMakeUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall CMake? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (^
    IF NOT "%cmake_root_dir%" == "" (rmdir /S /Q C:\cmake-3.9.3-win64-x64\)^
    ELSE (GOTO UserInputCMakeUninstallEnd)))^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputCMakeUninstallEnd)^
    ELSE (GOTO UserInputCMakeUninstallStart))
:UserInputCMakeUninstallEnd

::==============================================================================
:: Uninstall Visual Studio 2017
::==============================================================================
:UserInputVisualStudioUninstallStart
SET INPUT=
SET /P INPUT=^^^%\n%%\n%^%\n%Would you like to uninstall Visual Studio 2017? (Y/N) ^^^%\n%%\n%^%\n%Enter "Y" to uninstall.^^^%\n%%\n%^%\n%Enter "N" to skip: %=%
If /I "%INPUT%"=="y" (^
    IF %bool_vs_exist% == true (start /WAIT /d ".\EXTRA" vs_community__1560776263.1499642898.exe)^
    ELSE (GOTO UserInputVisualStudioUninstallEnd)))^
ELSE (^
    IF /I "%INPUT%"=="n" (GOTO UserInputVisualStudioUninstallEnd)^
    ELSE (GOTO UserInputVisualStudioUninstallStart))
:UserInputVisualStudioUninstallEnd




