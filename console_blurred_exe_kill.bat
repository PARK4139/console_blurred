:: kill 
wmic process where name="console_blurred.exe" delete
taskkill /f /im console_blurred.exe
taskkill /f /im python.exe