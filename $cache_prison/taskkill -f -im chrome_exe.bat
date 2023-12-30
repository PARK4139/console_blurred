echo "______________________________________________________________________________________________________________________________ minimized window
REM minimized s
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized
REM minimized e
echo "______________________________________________________________________________________________________________________________ getAdmin  
REM >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM if '%errorlevel%' NEQ '0' ( echo Requesting administrative privileges... goto UACPrompt 
REM ) else ( goto gotAdmin ) 
REM :UACPrompt 
	REM echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs" 
	REM set params = %*:"="" 
	REM echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" 
	REM "%temp%\getadmin.vbs" 
	REM del "%temp%\getadmin.vbs" 
	REM exit /B 
REM :gotAdmin
	REM pushd "%CD%"
	REM CD /D "%~dp0"
REM :------------------------------------------ below cript will acted as administrator mode ------------------------------------------ 
echo "______________________________________________________________________________________________________________________________ title
title %~n0
echo "______________________________________________________________________________________________________________________________ encording
chcp 65001 >nul
echo "______________________________________________________________________________________________________________________________ color
color df
echo "______________________________________________________________________________________________________________________________ echo
@echo off
echo "______________________________________________________________________________________________________________________________ variable
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyymmddhhmmss=%%i
set from=E:\500GB\do\utils\space that test\test_from
set to=E:\500GB\do\utils\space that test\test_to



taskkill /f /im chrome.exe