:: ADMIN SET UP
@REM  >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
@REM  if '%errorlevel%' NEQ '0' ( echo Requesting administrative privileges... goto UACPrompt
@REM  ) else ( goto gotAdmin )
@REM  :UACPrompt
@REM 	 echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
@REM 	 set params = %*:"=""
@REM 	 echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"
@REM 	 "%temp%\getadmin.vbs"
@REM 	 del "%temp%\getadmin.vbs"
@REM 	 exit /B
@REM  :gotAdmin
@REM 	 pushd "%CD%"
@REM 	 CD /D "%~dp0"
@REM  :------------------------------------------ below cript will acted as administrator mode ------------------------------------------




:: CONSOLE SET UP
@echo off            &&  :: CONSOLE ECHO SETTING
color df             &&  :: CONSOLE COLOR SETTING
chcp 65001 >nul      &&  :: KOREAN ENCODING SETTING
title %~dpnx0 >nul   &&  :: CONSOLE TITLE SET UP
@REM cls             &&  :: CONSOLE SCREEN CLEAR SETTING
@REM setlocal        &&  :: LOCAL ENVRIONMENT MODE SETTING


:: MAXIMIZED WINDOW SET UP
if not "%maximized%"=="" goto :maximized
set maximized=true
start /max cmd /C "%~dpnx0"
goto :EOF
:maximized

:: MINIMIZED WINDOW SET UP
@REM if not "%minimized%"=="" goto :minimized
@REM set minimized=true
@REM start /min cmd /C "%~dpnx0"
@REM goto :EOF
@REM :minimized





:: FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (SHORT WAY)
@REM cd c:\
@REM cd "%USERPROFILE%\Desktop\services"
@REM for /f "delims=" %%i in ('dir /s /b *%PROJECT_NAME%') do cd "%%i"


:: FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (FAST WAY)
@REM cd c:\
@REM cd "%USERPROFILE%\Desktop\services"
@REM dir /s /b *%PROJECT_NAME% > ".\%PROJECT_NAME%\PROJECT_DIRECTORY.txt"
@REM for /f "delims=" %%i in ('"type .\%PROJECT_NAME%\PROJECT_DIRECTORY.txt | findstr %PROJECT_NAME%"') do cd "%%i"


:: FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (FAST WAY)
@REM for /f "delims=" %%i in ('dir /s /b *%PROJECT_NAME%*') do cd "%%i"



:: RUN PYTHON VIRTUAL ENVIRONMENT
:: echo "%~dp0.venv\Scripts\activate.bat"
cmd /k call "%~dp0.venv\Scripts\activate.bat"


:: CONSOLE DEBUGGING SETTING
:: pause


:: 배치파일에서 argument 받기
:: set "FIRST_ARGUMENT=%1"
:: set "promised_space=      "
:: echo "park4139 command >%promised_space% FIRST_ARGUMENT:{%FIRST_ARGUMENT%}"
 

:: RUN PYTHON PROGRAM
:: python helper.py
:: python ".\helper.py"
:: python "%~dp0helper.py" %1
:: python ".\helper.py" %FIRST_ARGUMENT%  && :: 배치파일에서 argument 파이썬 프로그램에 넘겨서 실행

