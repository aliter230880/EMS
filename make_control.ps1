$c=@'
import asyncio
from bleak import BleakClient, BleakScanner

DEVICE_MAC='A4:34:F1:AB:D9:7C'
MOTOR_UUID='fff1'
MODES={1:'Anti-Aging',2:'Toning',3:'Spa',4:'Sculptor',5:'Massage',6:'Custom'}

async def send_ems_command(client,intensity,mode):
 command=bytearray([100,intensity,mode,128])
 try:
 await client.write_gatt_char(MOTOR_UUID,command)
 print(f'OK: {intensity}/{mode}')
 return True
 except Exception as e:
 print(f'ERR: {e}')
 return False

async def stop_device(client):
 return await send_ems_command(client,0,1)

print('ready')
'@
;[System.IO.File]::WriteAllText("$PWD\control_bear.py",$c,[System.Text.Encoding]::UTF8)