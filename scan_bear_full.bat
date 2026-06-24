@echo off 
echo ================================================ 
echo BEAR Full Scanner 
echo ================================================ 
echo. 
echo IMPORTANT: 
echo 1. CLOSE FOREO app on phone (disconnect device) 
echo 2. PRESS BEAR button to wake it up 
echo 3. Press any key when ready... 
pause >nul 
 
python scan_full.py 
 
pause
