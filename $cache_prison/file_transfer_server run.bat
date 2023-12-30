REM echo "___________________________________________________________________________________________________________ @echo s
@echo off
REM echo "___________________________________________________________________________________________________________ @echo e
echo "___________________________________________________________________________________________________________ common s
chcp 65001 >nul
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
set log_file=deploy.log
echo "___________________________________________________________________________________________________________ common e
echo "___________________________________________________________________________________________________________ minimized window s
REM minimized s
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized
echo "___________________________________________________________________________________________________________ minimized window e
echo "___________________________________________________________________________________________________________ opening log s
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
echo "server started tiem : %yyyyMMddHHmmss%" > %log_file%
hostname  > %log_file%
echo %cd% > %log_file%
ipconfig -all | find "192" > %log_file%
ipconfig -all | find "172" > %log_file%
ipconfig -all | find "172" > %log_file%
echo "___________________________________________________________________________________________________________ opening log e
echo "___________________________________________________________________________________________________________ info s
echo "server started tiem : %yyyyMMddHHmmss%"  
hostname  
echo %cd%  
ipconfig -all | find "192"
ipconfig -all | find "172"
ipconfig -all | find "172"
echo "___________________________________________________________________________________________________________ info e
echo "___________________________________________________________________________________________________________ s
py my_gtts.py "배포 게이트 오픈을 시작합니다"
py -m http.server 8000
py my_gtts.py "배포 게이트 오픈을 종료합니다"


taskkill -im alsong.exe -f
echo "___________________________________________________________________________________________________________ e

echo "___________________________________________________________________________________________________________ ending log s
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
echo "server started tiem : %yyyyMMddHHmmss%" > %log_file%
hostname  > %log_file%
echo %cd% > %log_file%
ipconfig -all | find "192" > %log_file%
ipconfig -all | find "172" > %log_file%
ipconfig -all | find "172" > %log_file%
echo "___________________________________________________________________________________________________________ ending log e