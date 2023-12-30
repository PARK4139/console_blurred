title %~n0
@echo off
chcp 65001 >nul
setlocal
echo "___________________________________________________________________________ URL s
set ip=172.30.1.85
REM set ip=172.30.1.255
REM set ip=172.30.1.92
set port=8000
set zip_file=deploy.zip
echo "___________________________________________________________________________ URL e 
echo "___________________________________________________________________________ directory s
set starting_directory=%cd%
cd ..
cd ..
mkdir "`"
cd "`"
mkdir "download.result"
cd "download.result"
set ending_directory=%cd%
echo "___________________________________________________________________________ directory e
echo "___________________________________________________________________________ s


cd %starting_directory%
py my_gtts.py "다운로드를 시작합니다"


cd %ending_directory%
call curl -O http://%ip%:%port%/%zip_file%


cd %starting_directory%
py my_gtts.py "다운로드를 완료하였습니다" 


cd %ending_directory%
call bandizip.exe bx %zip_file%


cd %starting_directory%
py my_gtts.py "압축해제를 완료하였습니다"


cd %ending_directory%
del %zip_file%


cd %starting_directory%
py my_gtts.py "압축파일 삭제를 완료하였습니다"


echo "___________________________________________________________________________ e
timeout 5
taskkill /im alsong.exe /f
REM pause