@echo off  
echo ==========================================  
echo FOREO API PROXY CAPTURE  
echo ==========================================  
echo IP addresses on this PC:  
ipconfig | findstr IPv4  
echo.  
echo Configure phone WiFi proxy:  
echo Hostname: 192.168.0.150  
echo Port: 8888  
echo.  
echo Starting proxy...  
python simple_http_proxy.py 
