import asyncio
from bleak import BleakScanner

async def scan_all():
    print('Scanning for BLE devices...')
    print('='*60)
    devices=await BleakScanner.discover(timeout=15.0)
    if not devices:
        print('No devices found!')
        print('Check Bluetooth adapter is working')
        return
    print(f'Found {len(devices)} device(s):\n')
    for d in devices:
        name=d.name or 'Unknown'
        if 'bear' in name.lower() or 'foreo' in name.lower() or 'a4:34' in d.address.lower():
            print(f'*** {name} - {d.address} (POSSIBLE MATCH!)')
        else:
            print(f'{name} - {d.address}')

if __name__=='__main__':
    asyncio.run(scan_all())
