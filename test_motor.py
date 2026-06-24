import asyncio
from bleak import BleakScanner, BleakClient

async def test():
    d = await BleakScanner.find_device_by_address('A4:34:F1:AB:D9:7C', timeout=20)
    if not d:
        print('NOT FOUND')
        return
    print('Connecting...')
    async with BleakClient(d, timeout=30) as c:
        await c.write_gatt_char('00000a0d-0000-1000-8000-00805f9b34fb', bytes.fromhex('01'), response=False)
        print('Wake sent')
        await asyncio.sleep(0.5)
        await c.write_gatt_char('00000a0f-0000-1000-8000-00805f9b34fb', b'eZxQX43wHKg2tJ', response=False)
        print('Activate sent')
        await asyncio.sleep(0.5)
        print('Sending MOTOR=3 (hex: 0a1132)')
        await c.write_gatt_char('0000fff2-0000-1000-8000-00805f9b34fb', bytes.fromhex('0a1132'), response=False)
        await asyncio.sleep(1)
        print('Sending EMS=05 (hex: 0a200105)')
        await c.write_gatt_char('0000fff2-0000-1000-8000-00805f9b34fb', bytes.fromhex('0a200105'), response=False)
        print('Commands sent! Wabt 5 sec...')
        await asyncio.sleep(5)
        print('Stopping...')
        await c.write_gatt_char('0000fff2-0000-1000-8000-00805f9b34fb', bytes.fromhex'0a1100'), response=False)
        print('Done!')

asyncio.run(test())
