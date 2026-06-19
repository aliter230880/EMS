import asyncio  
from bleak import BleakScanner, BleakClient  
  
async def scan_devices():  
print('Scanning BLE devices...')  
devices = await BleakScanner.discover(timeout=10.0)  
print(f'Found {len(devices)} devices')  
foreo_devices = []  
for device in devices:  
name = device.name or 'Unknown'  
if 'FOREO' in name.upper() or 'BEAR' in name.upper():  
foreo_devices.append(device)  
print(f'FOUND FOREO: {device.name} - {device.address}')  
return foreo_devices[0] if foreo_devices else None  
  
async def main():  
device = await scan_devices()  
if device:  
print(f'Ready to connect: {device.address}')  
  
asyncio.run(main())  
