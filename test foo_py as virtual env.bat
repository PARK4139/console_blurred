echo ________________________________________________________ ADMIN SET UP
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


echo ________________________________________________________ CONSOLE SET UP
@REM @echo on
@echo OFF
color df
chcp 65001 >nul      
title %~dpnx0 >nul  
@REM cls            
@REM setlocal         



@REM echo ________________________________________________________ MAXIMIZED WINDOW SET UP
@REM if not "%maximized%"=="" goto :maximized
@REM set maximized=true
@REM start /max cmd /C "%~dpnx0"
@REM goto :EOF
@REM :maximized


@REM echo ________________________________________________________ MINIMIZED WINDOW SET UP
@REM if not "%minimized%"=="" goto :minimized
@REM set minimized=true
@REM start /min cmd /C "%~dpnx0"
@REM goto :EOF
@REM :minimized


@REM echo ________________________________________________________ FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (SHORT WAY)
@REM cd c:\
@REM cd "%USERPROFILE%\Desktop\services"
@REM for /f "delims=" %%i in ('dir /s /b *%PROJECT_NAME%') do cd "%%i"


@REM echo ________________________________________________________ FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (FAST WAY)
@REM cd c:\
@REM cd "%USERPROFILE%\Desktop\services"
@REM dir /s /b *%PROJECT_NAME% > ".\%PROJECT_NAME%\PROJECT_DIRECTORY.txt"
@REM for /f "delims=" %%i in ('"type .\%PROJECT_NAME%\PROJECT_DIRECTORY.txt | findstr %PROJECT_NAME%"') do cd "%%i"


@REM echo ________________________________________________________ FIND PROJECT DIRECTORY AND CHANGE DIRECTORY TO PROJECT DIRECTORY SETTING (FAST WAY)
@REM for /f "delims=" %%i in ('dir /s /b *%PROJECT_NAME%*') do cd "%%i"



echo ________________________________________________________ RUN PYTHON VIRTUAL ENVIRONMENT
echo "%~dp0.venv\Scripts\activate.bat"
call "%~dp0.venv\Scripts\activate.bat"



echo ________________________________________________________ CHECK BATCH ARGUEMENT
echo %1

echo ________________________________________________________ SET PYTHON FILE TO TEST AS BATCH SCRIPT VARIABLE VIA BATCH SCRIPT ARGUMENT
set foo_py=%1

echo ________________________________________________________ CHECK BATCH VARIABLE
echo %foo_py%


echo ________________________________________________________ RUN PYTHON TEST PROGRAM
echo "%~dp0\%foo_py%"
python "%~dp0\%foo_py%"

echo ________________________________________________________ CONSOLE DEBUGGING SETTING
@REM pause
exit



