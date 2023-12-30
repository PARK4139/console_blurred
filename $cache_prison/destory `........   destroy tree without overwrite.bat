 
set path_destination=%cd%
REM c:
REM d:
REM e:
REM f:
cd "`"
mkdir "`"
for /r %%i in (*.*) do move "%%i" "%path_destination%"
cd ..
for /f "usebackq delims=" %%i in (`"dir /s /b /ad | sort /r"`) do rd "%%i" 2>NUL 
 