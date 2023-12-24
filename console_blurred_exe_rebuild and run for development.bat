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
@REM @echo off >nul
color df >nul
chcp 65001 >nul 
title %~dpnx0 >nul
@REM cls >nul
@REM setlocal >nul


:: MAXIMIZED WINDOW SET UP
@REM if not "%maximized%"=="" goto :maximized
@REM set maximized=true
@REM start /max cmd /C "%~dpnx0"
@REM goto :EOF
@REM :maximized

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
:: call "%~dp0.venv\Scripts\activate.bat"
call ".\.venv\Scripts\activate.bat"


:: BUILD FOR DEVELOPMENT
echo y | del ".\console_blurred.exe"
echo y | rmdir /s ".\_internal"
echo y | rmdir /s ".\build"
echo y | rmdir /s ".\dist"
echo y | rmdir /s ".\dist\console_blurred\_internal\$cache_database"
echo y | rmdir /s ".\dist\console_blurred\_internal\$cache_log"
echo y | rmdir /s ".\dist\console_blurred\_internal\$cache_mp3"
echo y | rmdir /s ".\dist\console_blurred\_internal\$cache_png"
echo y | rmdir /s ".\dist\console_blurred\_internal\$cache_tools"
echo y | rmdir /s ".\dist\console_blurred\_internal\$cache_txt"
:: pyinstaller --windowed -i ".\$cache_png\icon.PNG" console_blurred.py
pyinstaller -i ".\$cache_png\icon.PNG" console_blurred.py
echo d | xcopy ".\$cache_database" ".\dist\console_blurred\_internal\$cache_database" /e /h /k
echo d | xcopy ".\$cache_log" ".\dist\console_blurred\_internal\$cache_log" /e /h /k
echo d | xcopy ".\$cache_mp3" ".\dist\console_blurred\_internal\$cache_mp3" /e /h /k
echo d | xcopy ".\$cache_png" ".\dist\console_blurred\_internal\$cache_png" /e /h /k
echo d | xcopy ".\$cache_tools" ".\dist\console_blurred\_internal\$cache_tools" /e /h /k
echo d | xcopy ".\$cache_txt" ".\dist\console_blurred\_internal\$cache_txt" /e /h /k
echo d | xcopy ".\pkg_park4139" ".\dist\console_blurred\_internal\pkg_park4139" /e /h /k
@rem echo y | echo d | xcopy ".\$cache_zip" ".\dist\console_blurred\_internal\$cache_zip" /e /h /k
explorer ".\dist\console_blurred\console_blurred.exe"
@REM echo a | move ".\dist\console_blurred\console_blurred.exe" ".\"
@REM echo a | move ".\dist\console_blurred\_internal" ".\"
@REM echo y | rmdir /s ".\build"
@REM echo y | rmdir /s ".\dist"
@REM explorer ".\console_blurred.exe

timeout 66