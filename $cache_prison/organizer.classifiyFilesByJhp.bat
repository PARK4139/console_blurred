@REM echo "________________________________________________________________ code page setting s"
@REM chcp 65001 >nul
@REM echo "________________________________________________________________ code page setting e"
echo "________________________________________________________________ minimized window s"
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized
echo "________________________________________________________________ minimized window e"
echo "________________________________________________________________ title s"
title %~n0
echo "________________________________________________________________ title e"
@REM echo "________________________________________________________________ echo off s"
@REM @echo off
@REM echo "________________________________________________________________ echo off e"
@REM echo "________________________________________________________________ idea s"
@REM organize file by jhp.py 로 만들 계획이 있음.
@REM 중복이름의 파일이 덮어쓰여지는 문제를 해결하도록 directory 가 없는지 확인로직 필요.+ 파일에 timestamp 를 ms 까지 붙여서 덮어쓰는 문제 해결하는 것도 고민해보기
@REM 어떠한 디렉토리도 없으면 파일 정리 시작. 
@REM echo "________________________________________________________________ idea e"
@REM echo "________________________________________________________________  organize files by extension s"
@REM for %%i in (*.*) do if not "%~nx0"=="%%~nxi" (
@REM if not exist "%%~xi\" md "%%~xi"
@REM move "%%i" "%%~xi"
@REM ) 
@REM echo "________________________________________________________________  organize files by extension e"



@REM mkdir "`" 


for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
mkdir "`imgs - %yyyyMMddHHmmss%"
for %%i in (*.jpg *.png *.webp *.jfif *.webp *.gif *.jpeg *.bmp *.jfif *.tif) do move "%%i" "`imgs - %yyyyMMddHHmmss%"

     


for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
mkdir "`videoes - %yyyyMMddHHmmss%"
for %%i in (*.avi *.mp4 *.mkv *.webm *.dpl) do move "%%i" "`videoes - %yyyyMMddHHmmss%"

 
 
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
mkdir "`sounds - %yyyyMMddHHmmss%"
for %%i in (*.mp3 *.flac *.weba *.m4a *.ogg *.wav) do move "%%i" "`sounds - %yyyyMMddHHmmss%"



 
 
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
mkdir "`document - %yyyyMMddHHmmss%"
@rem for %%i in (*.show *.md *.txt *.xmind *.pptx *.ppt *.xls *.xlsm *.hwp) do move "%%i" "`document - %yyyyMMddHHmmss%"
for %%i in (*.md *.txt *.xmind *.ini) do move "%%i" "`document - %yyyyMMddHHmmss%"





@REM timeout 30
@REM move "`imgs - %yyyyMMddHHmmss%" "`"
@REM move "`videoes - %yyyyMMddHHmmss%" "`"
@REM move "`sounds - %yyyyMMddHHmmss%" "`"
@REM move "`document - %yyyyMMddHHmmss%" "`"
        

echo "________________________________________________________________ 불필요한 파일 강제 삭제 s"
del /f "C:\Users\Public\Desktop\BLUEMAX Client.lnk"
for /f "usebackq delims=" %%i in (`dir /b /s "最 新 位 址 獲 取.txt"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "聚 合 全 網 H 直 播.html"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "社 區 最 新 情 報.mp4"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "x u u 9 2 .c o m.mp4"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "PotPlayerMini64.dpl"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "PRARBG.txt"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "RARBG_DO_NOT_MIRROR.exe"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "www.btranking.top - 최초배포.url"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "AV大平台.url"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "RARBG.txt"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "RARBG_DO_NOT_MIRROR.exe"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "www.hhd800.com.txt"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "Alpha.2018.1080p.BluRay.H264.AAC.mp4.nfo"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "www.YTS.AM.jpg"`) do del /f "%%i" 2>NUL
for /f "usebackq delims=" %%i in (`dir /b /s "更多精品獨家資源下載.mht"`) do del /f "%%i" 2>NUL


:: .srt 파일을 순회하며 모두 삭제
for /f "usebackq delims=" %%i in (`dir /b /s "*.srt"`) do del /f "%%i" 2>NUL

:: .nfo 파일을 순회하며 모두 삭제
for /f "usebackq delims=" %%i in (`dir /b /s "*.nfo"`) do del /f "%%i" 2>NUL

:: 빈폴더를 순회하며 모두 삭제
echo "________________________________________________________________ 불필요한 파일 강제 삭제 e"








@REM echo "________________________________________________________________  pause s"
@REM pause
@REM echo "________________________________________________________________  pause e"