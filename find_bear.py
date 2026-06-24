import asyncio
from bleak import BleakScanner

async def find_bear():
    print('== FINDING BEAR A4:34:F1:AB:D9:7C ==')
    print('Press BEAR button NOW!\n')
    for attempt in range(5):
        print(f'Attempt {attempt+1}/5 - scanning 20 seconds...')
        device = await BleakScanner.find_device_by_address('A4:34:F1:AB:D9:7C', timeout=20.0)
        if device:
            print(f'\n*** FOUND: {device.name} - {device.address} ***')
            return
        print('Not found, retrying...\n')
        await asyncio.sleep(1)
    print('\nNOT FOUND after 5 attempts')
    print('CHECK: 1.Device ON  2.Not connected to phone  3.Bluetooth OK')

asyncio.run(find_bear())

