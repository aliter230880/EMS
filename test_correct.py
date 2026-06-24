import asyncio 
from bleak import BleakClient,BleakScanner 
DEVICE_MAC='A4:34:F1:AB:D9:7C' 
SERIAL='eZxQX43wHKg2tJ' 
WAKE_UUID='00000a0d-0000-1000-8000-00805f9b34fb' 
ACT_UUID='00000a0f-0000-1000-8000-00805f9b34fb' 
MODE_UUID='0000fff2-0000-1000-8000-00805f9b34fb' 
MOTOR_PREFIX='0a11' 
EMS_PREFIX='0a20' 
MOTOR_LEVELS=['00','28','32','3C','46','50'] 
async def wake(c): 
await c.write_gatt_char(WAKE_UUID,bytes.fromhex('01'),response=False);print('wake') 
async def act(c): 
await c.write_gatt_char(ACT_UUID,'eZxQX43wHKg2tJ'.encode('ascii'),response=False);print('act') 
async def motor(c,i): 
h=MOTOR_PREFIX+MOTOR_LEVELS[i];await c.write_gatt_char(MODE_UUID,bytes.fromhex(h),response=False);print(f'M:{i} {h}') 
async def ems(c,i): 
h=EMS_PREFIX+('01' if i>0 else '00')+f'{i:02x}';await c.write_gatt_char(MODE_UUID,bytes.fromhex(h),response=False);print(f'E:{i} {h}') 
async def test(): 
from bleak import BleakScanner 
d=await BleakScanner.find_device_by_address(DEVICE_MAC,timeout=20) 
if not d:print('NOT FOUND');return 
async with BleakClient(d,timeout=30) as c: 
await wake(c);await asyncio.sleep(0.5) 
await act(c);await asyncio.sleep(0.5) 
print('TEST: motor=3, ems=5') 
await ems(c,5);await asyncio.sleep(0.1) 
await motor(c,3);await asyncio.sleep(3) 
print('STOP') 
await motor(c,0);await ems(c,0) 
asyncio.run(test())
