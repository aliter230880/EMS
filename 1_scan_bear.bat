@echo off 
echo ================================ 
echo STEP 1: BEAR Device Scanner 
echo ================================ 
echo. 
echo BEFORE RUNNING: 
echo 1. Press BEAR button (turn ON) 
echo 2. Close FOREO app on phone 
echo 3. Turn OFF Bluetooth on phone 
echo. 
pause 
echo Scanning... 
python scan_full.py 
echo. 
pause
