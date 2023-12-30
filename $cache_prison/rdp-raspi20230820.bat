@echo off
echo "___________________________________________________________________________________ echo
echo "___________________________________________________________________________________ title
title %~n0
echo "___________________________________________________________________________________ encoding
chcp 65001 >nul
echo "___________________________________________________________________________________ 윈도우 원격  접속 
@REM explorer https://remotedesktop.google.com/access 
@rem start /b /max mstsc /admin /v 172.30.1.78:3389 /multimon   
REM start /b /max mstsc /admin /w:640 /h:350 /v 172.30.1.78:3389 /NoConsentPrompt
REM start /b /max mstsc /admin /w:960 /h:540 /v 172.30.1.78:3389 /NoConsentPrompt
REM start /b /max mstsc /admin /w:960 /h:540 /v 172.30.1.78:3389 /NoConsentPrompt 
start /b /max mstsc /admin /w:960 /h:1080 /v 172.30.1.78:3389 /NoConsentPrompt 
@REM start /b /max mstsc /admin /v 211.221.139.87:3389 /multimon
REM echo raspi20230820 | clip.exe
REM echo "symetrical" | clip.exe
ssh raspi20230820@172.30.1.78 
echo "___________________________________________________________________________________ pause
REM pause
