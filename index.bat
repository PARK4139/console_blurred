:: ADMIN MODE SETTING
:: >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
:: if '%errorlevel%' NEQ '0' ( echo Requesting administrative privileges... goto UACPrompt
:: ) else ( goto gotAdmin )
:: :UACPrompt
:: 	echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
:: 	set params = %*:"=""
:: 	echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"
:: 	"%temp%\getadmin.vbs"
:: 	del "%temp%\getadmin.vbs"
:: 	exit /B
:: :gotAdmin
:: 	pushd "%CD%"
:: 	CD /D "%~dp0"
:: :------------------------------------------ below cript will acted as administrator mode ------------------------------------------


:: CONSOLE SET UP
@echo off          :: CONSOLE ECHO SETTING
color df           :: CONSOLE COLOR SETTING
chcp 65001 >nul && :: KOREAN ENCODING SETTING
title %~dpnx0 >nul     :: CONSOLE TITLE SET UP
:: cls                :: CONSOLE SCREEN CLEAR SETTING
:: setlocal           :: LOCAL ENVRIONMENT MODE SETTING



:: MAXIMIZED WINDOW SET UP
if not "%maximized%"=="" goto :maximized
set maximized=true
start /max cmd /C "%~dpnx0"
goto :EOF
:maximized


:: MINIMIZED WINDOW SET UP
:: if not "%minimized%"=="" goto :minimized
:: set minimized=true
:: start /min cmd /C "%~dpnx0"
:: goto :EOF
:: :minimized


:: PROJECT SET UP
set "PROJECT_NAME=PYTHON TEST ARCHIVE"


:: FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (FAST WAY)
:: cd c:\
:: for /f "delims=" %%i in ('dir /s /b *%PROJECT_NAME%') do cd "%%i"


:: FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (SLOW WAY)
:: cd c:\
:: cd "%USERPROFILE%\Desktop\services"
:: dir /s /b *%PROJECT_NAME% > ".\%PROJECT_NAME%\PROJECT_DIRECTORY.txt"
:: for /f "delims=" %%i in ('"type .\%PROJECT_NAME%\PROJECT_DIRECTORY.txt | findstr %PROJECT_NAME%"') do cd "%%i"



:: RUN PYTHON VIRTUAL ENVIRONMENT SETTING
call ".\.venv\Scripts\activate.bat"
 

:: RUN PYTHON PROGRAM SETTING
python ".\index.py"


:: CONSOLE DEBUGGING SETTING
pause