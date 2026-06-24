CODE = '''import asyncio 
from bleak import BleakClient, BleakScanner 
 
DEVICE_MAC = 'A4:34:F1:AB:D9:7C' 
MOTOR_UUID = 'fff1'
MODES = {1: 'Anti-Aging', 2: 'Toning', 3: 'Spa', 4: 'Sculptor', 5: 'Massage', 6: 'Custom'} 
 
async def send_ems_command(client, intensity, mode): 
command = bytearray([100, intensity, mode, 128]) 
try: 
await client.write_gatt_char(MOTOR_UUID, command) 
print(f'OK: intensity={intensity}, mode={mode}') 
return True 
except Exception as e: 
print(f'ERROR: {e}') 
return False
