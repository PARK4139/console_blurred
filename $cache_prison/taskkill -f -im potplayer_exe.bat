:: kill_all_cmd_exe
wmic process where name="PotPlayer64.exe" delete
taskkill /im "PotPlayer64.exe" /f