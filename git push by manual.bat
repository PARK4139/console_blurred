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
:: set commit_ment=REFER TO README.md (commited at %yyyyMMddHHmmss%)
:: set commit_ment=Members API 작성 및 로컬 테스트 완료
:: set commit_ment=FastAPI 기반 API 작성 및 라우팅 및 데이터 유효성 로컬 테스트 일부 완료
:: set commit_ment=nav-items API aws 배포 완료
:: set commit_ment="README.md" 업데이트
:: set commit_ment=Flask 웹 FastApi 웹 마이그레이션 시작(회원가입/로그인 API)
:: set commit_ment=Flask 웹 FastApi 웹 마이그레이션 로컬 테스트 완료(회원가입/로그인 API)
set commit_ment=윈도우용 커스텀 패키지/윈도우용 파이썬 프로젝트 추출


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