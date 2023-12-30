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
:: 우선 불행히도 pyinstaller 로 build 시에 gtts 모듈은 동작하지 않는 것 같다...하..
:: 프로젝트 파일 빽업
:: Park4139.troubleshoot() 에서 pause() 활성화 설정
:: Park4139.trouble_shoot("%%%FOO%%%") 에 %%%FOO%%% 부분 autofill dev tool 적용
:: run cmd.exe as user  와.... 빌드 시에는 run cmd.exe as admin 하면 안된다 경로가 시스템경로로 나온다. 당연히 admin으로 해야하는 줄 알았는데.. 완전 오판이었다. 하지만 permission 다룰 때는 admin 써야한다.
:: 고로 둘 다 써야한다.
cd "%USERPROFILE%"
cd ".\Desktop\services\archive_py"
@rem echo %cd% | clip.exe
:: 매우주의하며 수행할 것 taskkill /f /im pycharm64.exe
call ".\.venv\Scripts\activate.bat"
:: echo y | del ".\console_blurred.exe"
echo y | rmdir /s ".\build"
echo y | rmdir /s ".\dist"
echo y | rmdir /s ".\_internal"
python -m pip install --upgrade pip
pip install pyinstaller --upgrade
pyinstaller -i "%USERPROFILE%\Desktop\services\archive_py\$cache_png\icon.PNG" console_blurred.py
:: pyinstaller --windowed -i "%USERPROFILE%\Desktop\services\archive_py\$cache_png\icon.PNG" console_blurred.py
:: pyinstaller --windowed -i ".\$cache_png\icon.PNG" console_blurred.py
:: pyinstaller -i ".\$cache_png\icon.PNG" console_blurred.py
echo d | xcopy ".\$cache_database" ".\dist\console_blurred\_internal\$cache_database" /e /h /k
echo d | xcopy ".\$cache_log" ".\dist\console_blurred\_internal\$cache_log" /e /h /k
echo d | xcopy ".\$cache_mp3" ".\dist\console_blurred\_internal\$cache_mp3" /e /h /k
echo d | xcopy ".\$cache_png" ".\dist\console_blurred\_internal\$cache_png" /e /h /k
echo d | xcopy ".\$cache_tools" ".\dist\console_blurred\_internal\$cache_tools" /e /h /k
echo d | xcopy ".\$cache_txt" ".\dist\console_blurred\_internal\$cache_txt" /e /h /k
echo d | xcopy ".\pkg_yt_dlp" ".\dist\console_blurred\_internal\pkg_yt_dlp" /e /h /k
echo d | xcopy ".\pkg_park4139" ".\dist\console_blurred\_internal\pkg_park4139" /e /h /k
echo d | xcopy ".\$cache_fonts" ".\dist\console_blurred\_internal\$cache_fonts" /e /h /k
echo d | xcopy ".\$cache_work_for_music" ".\dist\console_blurred\_internal\$cache_work_for_music" /e /h /k
@rem echo y | echo d | xcopy ".\$cache_zip" ".\dist\console_blurred\_internal\$cache_zip" /e /h /k
:: cd "%USERPROFILE%"
:: cd ".\Desktop\services\archive_py"
:: PowerShell -Command "Start-Process cmd -Verb RunAs"    :: 아래 코드는 배치파일용 코드로 바꿔야 함.
cd "%USERPROFILE%"
cd ".\Desktop\services\archive_py"
:: echo d | xcopy ".\build" "%USERPROFILE%\DESKTOP\build" /e /h /k
echo d | xcopy ".\dist" "%USERPROFILE%\DESKTOP\dist" /e /h /k
echo f | xcopy ".\console_blurred_exe_run.bat" "%USERPROFILE%\DESKTOP\dist\console_blurred_exe_run.bat" /e /h /k
echo f | xcopy ".\console_blurred_exe_kill.bat" "%USERPROFILE%\DESKTOP\dist\console_blurred_exe_kill.bat" /e /h /k
echo y | rmdir /s ".\build"
echo y | rmdir /s ".\dist"
echo y | rmdir /s ".\_internal"
explorer "%USERPROFILE%\DESKTOP\dist\console_blurred\console_blurred.exe"

cd "%USERPROFILE%\DESKTOP"
call "run deploy server for local network.bat"
pause
:: deactivate.bat
:: exit
timeout 66