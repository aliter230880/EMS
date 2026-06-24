import asyncio
from bleak import BleakScanner

async def scan():
    print('=== BEAR SCANNER ===')
    print('Press BEAR button NOW!')
    print('Scanning 30 seconds...\n')
    devices = await BleakScanner.discover(timeout=30.0)
    print(f'Found {len(devices)} devices:\n')
    found_bear = False
    for d in devices:
        name = d.name or 'Unknown'
        if 'a4:34' in d.address.lower() or 'bear' in name.lower():
            print(f'*** BEAR: {name} - {d.address}')
            found_bear = True
        else:
            print(f'  {name} - {d.address}')
    if not found_bear:
        print('\nWARNING: BEAR device not found!')
        print('Check: 1.Device ON  2.Not connected to phone  3.Bluetooth adapter OK')

asyncio.run(scan())

