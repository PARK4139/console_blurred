:: CONSOLE SETTING
title %~n0
color df
chcp 65001 >nul
@echo off
@rem @echo on
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
cls


:: MINIMIZED WINDOW SETTING
:: if not "%minimized%"=="" goto :minimized
:: set minimized=true
:: start /min cmd /C "%~dpnx0"
:: goto :EOF
:: :minimized


:: COMMIT MENT SETTING 
set commit_ment=REFER TO README.md (commited at %yyyyMMddHHmmss%)


:: GIT PUSH
git add *  
git commit -m "%commit_ment%"
git push -u origin main
git status | find "working tree clean" 



:: GET PROJECT_DIRECTORY
SET PROJECT_DIRECTORY=%cd%
for %%F in ("%CD%") do set "PROJECT_DIRECTORY_DIRNAME=%%~nxF"



:: CHECK GIT HUB PUSH DONE (Now)
explorer https://github.com/Park4139/%PROJECT_DIRECTORY_DIRNAME%



:: DEBUG SET UP
:: timeout 600