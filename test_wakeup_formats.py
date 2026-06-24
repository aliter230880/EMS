import asyncio
from bleak import BleakClient, BleakScanner

DEVICE_MAC='A4:34:F1:AB:D9:7C'
WAKE_UP_UUID='00000a0d-0000-1000-8000-00805f9b34fb'

async def test_wakeup():
    print('FOREO BEAR - Testing different wake-up formats')
    print('='*60)
    device=await BleakScanner.find_device_by_address(DEVICE_MAC,timeout=15.0)
    if not device:
        print('Device not found')
        return
    print(f'Found: {device.name or device.address}')
    async with BleakClient(device,timeout=30.0) as client:
        if not client.is_connected:
            print('Connection failed')
            return
        print('Connected!')
        print()
        
        formats=[
            ('HEX byte 0x01',bytes.fromhex
'01')),
            ('ASCII string "01"',b'01'),
            ('Raw byte 1',bytes([1])),
            ('HEX byte 0x040',bytes.fromhex
'0001')),
            ('ASCII "0001"',b'0001'),
        ]
        
        for desc,data in formats:
            print(f'Trying: {desc} -> {data.hex()}')
            try:
                await client.write_gatt_char(WAKE_UP_UUID,data,response=False)
                print('Sent successfully!')
                print('Check if 5 LEDs turned on?')
                input('Press ENTER to try next format...')
            except Exception as e:
                print(f'FAILED: {e}')
                print()
        
        print('Test complete!')

if __name__=='__main__':
    asyncio.run(test_wakeup())
