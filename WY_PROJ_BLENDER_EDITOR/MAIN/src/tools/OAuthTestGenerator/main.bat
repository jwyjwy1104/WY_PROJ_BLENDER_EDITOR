::==============================================================================
:: Main run batch file to run current project makefile with data loaded from 
:: the config XML file.
::==============================================================================
:: Lead Programmer   : Samil Chai (Copyright)
:: Junior Programmer : Nick Jang
:: 
:: Created Date: 2017-11-27
:: Last Updated: 2017-11-28
:: Desccription: 
::    This file generates the main makefile with the data loaded from
::    the config XML file where all the unit test cases related data values are
::    stored.
::    
::==============================================================================
@echo off
::==============================================================================
:: Read the data.config file to generate the makefile for which each classes' 
:: unit test case generating command is executed.
:: So the user can just append the XML data value to the data.config 
:: then this batch file will automatically create the makefile for each classes
:: implemented in the data.config file so the project main run_test.bat
:: executes the main makefile in this sub project OAuthTestGenerator to
:: generate and execute the unit test cases.
::==============================================================================

::==============================================================================
:: Init data structures to be used
::==============================================================================
:: To use array in batch file i need these line of code.
setlocal enabledelayedexpansion

:: Classes array
SET classes=()
:: Array of makefile name of classes
SET classes_makefile_name=()
:: Counter of the classes array
SET index=0

::==============================================================================
:: Read from data.config file and store the classes name into the array
::==============================================================================
for /F tokens^=2^,3^,5^,7^,9delims^=^<^"^= %%a in (data.config) do (IF "%%a" equ "class" (set /A index+=1 && SET classes[!index!]=%%b))

:: Store the makefile name for each classes loaded from config file
for /l %%n in (1,1,%index%) do (SET classes_makefile_name[%%n]=make_!classes[%%n]!)


:: Reset makefile for each classes
for /l %%n in (1,1,%index%) do (
    (
    echo(all:
    )> !classes_makefile_name[%%n]!
)



::==============================================================================
:: Delete data_terminated.txt file to be read on each makefile
:: to decide whether to terminate current makefile process
:: if progress bar is terminated by user
:: Progress bar will create data_terminated.txt so the paralle makefile
:: process will be terminated.
::==============================================================================
if exist data_terminated.txt (del data_terminated.txt)
if exist data_generated.txt (del data_generated.txt)

:: Delete the result file that will be generated through oauth_test_case_generator_executor.py
del C:\Users\Nickj\Desktop\WY_PROJ_BLENDER_EDITOR\WY_PROJ_BLENDER_EDITOR\MAIN\src\tools\OAuthTestGenerator\OAuthTestGenerator_Failed.txt
:: Delete the result file that will be generated through oauth_test_case_generator_executor.py
del C:\Users\Nickj\Desktop\WY_PROJ_BLENDER_EDITOR\WY_PROJ_BLENDER_EDITOR\MAIN\src\tools\OAuthTestGenerator\OAuthTestGenerator_Succeeded.txt

::==============================================================================
:: 1. Compare class names
:: 2. Reading data from data.config
:: 	First  element value  "title"     	 = %%b
:: 	Second element value  "url_id"    	 = %%c
:: 	Third  element value  "sheetname" 	 = %%d
:: 	Fourth element value  "class" 		 = %%e
:: 	Fifth  element value  "result_filepath"  = %%f
:: 3. If Fourth element value  "class" %%e is the class loaded then create
::    makefile with class name appended to "make_" to separate the makefile 
::    for each classes indicated in XML file.
:: 4. Write %%b title string to data_generated.txt so the progress bar will
::    read from data_generated.txt to show the process to users.
::==============================================================================
for /l %%n in (1,1,%index%) do (

    for /F tokens^=2^,3^,5^,7^,9^,11delims^=^<^"^= %%a in (data.config) do (
        IF "%%a" equ "title" (
            IF "%%e" equ "!classes[%%n]!" (
                (
                echo(	python oauth_test_case_generator_manager.py \
                echo(	^-title "%%b" \
                echo(	^-ssurl https://docs.google.com/spreadsheets/d/%%c/edit#gid=0 \
                echo(	^-feed %%d \
                echo(	^-app WY_PROJ_BLENDER_EDITOR_OAUTH_CLIENT \
                echo(	^>^> %cd%\%%f
                echo(	^@echo %%b ^>^> data_generated_!classes[%%n]!.txt
                echo(	^if exist data_terminated.txt (exit 1^)
                echo(	
                )>> !classes_makefile_name[%%n]!
            )
        )
    )
)




::==============================================================================
:: Pass the list of classes indicated in data.config file to the 
:: OAuthTestCaseGenerator interface Tkinter application
:: oauth_test_case_generator_interface.pyw in order to let the user choose the
:: specific classes for testing.
::==============================================================================
SET classes_name_argument_str=
for /l %%n in (1,1,%index%) do (
    SET classes_name_argument_str=!classes_name_argument_str!!classes[%%n]! 
)
python oauth_test_case_generator_interface.pyw %classes_name_argument_str%
























::==============================================================================
:: Original code.
::==============================================================================
goto :comment1
::==============================================================================
:: Reset data_generated.txt file to be read on progress bar.
::==============================================================================
(
echo(
)> data_generated.txt

::==============================================================================
:: Create main makefile which executes the generated sub makefiles
::==============================================================================
(
echo(all: progress_bar makes
echo(progress_bar:
echo(	python oauth_test_case_generator_progressbar.py
echo(makes:
)> makefile
for /l %%n in (1,1,%index%) do (
    (
    echo(	make -f !classes_makefile_name[%%n]! 
    )>> makefile
)

::==============================================================================
:: Execute makefile targets in parallel with "-j" option
::==============================================================================
make -j
:comment1
