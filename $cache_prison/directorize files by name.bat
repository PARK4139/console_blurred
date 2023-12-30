chcp 65001 >nul




c: 
cd "C:\Users\JungHoonPark\Desktop\`" 



pause
for %%i in (*) do (
 if not "%%~ni" == "?????" (
  md "%%~ni" && move "%%~i" "%%~ni"
 )
)

