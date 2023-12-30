@echo off
echo "___________________________________________________________________________________ echo
echo "___________________________________________________________________________________ title
title %~n0
echo "___________________________________________________________________________________ encoding
chcp 65001 >nul
echo "___________________________________________________________________________________ 윈도우 원격 접속, foo.rdp 없이
explorer https://remotedesktop.google.com/access
@REM start /b /max mstsc /admin /v 172.30.1.58:3389 /multimon /NoConsentPrompt
@REM start /b /max mstsc /admin /v 172.30.1.65:3389 /multimon /NoConsentPrompt
@REM start /b /max mstsc /admin /v 211.221.139.87:33899 /multimon /NoConsentPrompt
@REM start /b /max mstsc /admin /v 211.221.139.87:33899 /multimon /NoConsentPrompt
start /b /max mstsc /admin /v 172.30.1.50:3389 /multimon /NoConsentPrompt
start /b /max mstsc /admin /v 172.30.1.61:3389 /multimon /NoConsentPrompt
start /b /max mstsc /admin /v WIN10PROPC3:3389 /multimon /NoConsentPrompt
start /b /max mstsc /admin /v DESKTOP-3UKV75U:3389 /multimon /NoConsentPrompt
echo "___________________________________________________________________________________ pause
REM pause
