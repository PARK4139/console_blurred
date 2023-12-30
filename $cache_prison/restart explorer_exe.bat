:: kill_all_cmd_exe
wmic process where name="explorer.exe" delete
taskkill /im "explorer.exe" /f 
start explorer.exe 