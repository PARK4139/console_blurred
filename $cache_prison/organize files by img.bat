@echo off
echo "______________________________________________________________________________________________________________________________ echo
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
echo "______________________________________________________________________________________________________________________________ variable
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyymmddhhmmss=%%i
set from=E:\500GB\do\utils\space that test\test_from
set to=E:\500GB\do\utils\space that test\test_to



echo "imgs 중복문제해결코드 
ren "imgs" "imgs - %yyyymmddhhmmss%"


:: png
setlocal
set foo =.png
for %%i in (*.png) do if not "%~nx0"=="%%~nxi" (
if not exist "%%~xi\" md "%%~xi"
move "%%i" "%%~xi"
) 
set as=imgs
mkdir %as%
set from_path=%cd%
set to_path=%cd%\%as%
cd .png
move "*.png" "%to_path%"
cd %from_path% 
rmdir .png  


:: jpg
setlocal
set foo =.jpg
for %%i in (*.jpg) do if not "%~nx0"=="%%~nxi" (
if not exist "%%~xi\" md "%%~xi"
move "%%i" "%%~xi"
) 
set as=imgs
mkdir %as%
set from_path=%cd%
set to_path=%cd%\%as%
cd .jpg
move "*.jpg" "%to_path%"
cd %from_path% 
rmdir .jpg  




:: jfif
setlocal
set foo =.jfif
for %%i in (*.jfif) do if not "%~nx0"=="%%~nxi" (
if not exist "%%~xi\" md "%%~xi"
move "%%i" "%%~xi"
) 
set as=imgs
mkdir %as%
set from_path=%cd%
set to_path=%cd%\%as%
cd .jfif
move "*.jfif" "%to_path%"
cd %from_path% 
rmdir .jfif  



:: webp
setlocal
set foo =.webp
for %%i in (*.webp) do if not "%~nx0"=="%%~nxi" (
if not exist "%%~xi\" md "%%~xi"
move "%%i" "%%~xi"
) 
set as=imgs
mkdir %as%
set from_path=%cd%
set to_path=%cd%\%as%
cd .webp
move "*.webp" "%to_path%"
cd %from_path% 
rmdir .webp  



:: gif
setlocal
set foo =.gif
for %%i in (*.gif) do if not "%~nx0"=="%%~nxi" (
if not exist "%%~xi\" md "%%~xi"
move "%%i" "%%~xi"
) 
set as=imgs
mkdir %as%
set from_path=%cd%
set to_path=%cd%\%as%
cd .gif
move "*.gif" "%to_path%"
cd %from_path% 
rmdir .gif  



:: jpeg
setlocal
set foo =.jpeg
for %%i in (*.jpeg) do if not "%~nx0"=="%%~nxi" (
if not exist "%%~xi\" md "%%~xi"
move "%%i" "%%~xi"
) 
set as=imgs
mkdir %as%
set from_path=%cd%
set to_path=%cd%\%as%
cd .jpeg
move "*.jpeg" "%to_path%"
cd %from_path% 
rmdir .jpeg  



ren "imgs" "imgs - %yyyymmddhhmmss%"

