import asyncio
from bleak import BleakClient, BleakScanner

DEVICE_MAC='A4:34:F1:AB:D9:7C'

async def dump_services():
    print(f'Searching {DEVICE_MAC}...')
    device=await BleakScanner.find_device_by_address(DEVICE_MAC,timeout=10.0)
    if not device:
        print('Device not found')
        return
    print(f'Found: {device.name or device.address}')
    print('Connecting...')
    async with BleakClient(device,timeout=30.0) as client:
        if not client.is_connected:
            print('Connection failed')
            return
        print('Connected!')
        print('='*60)
        print('Services and Characteristics:')
        print('='*60)
        for svc in client.services:
            print(f'\nSERVICE: {svc.uuid}')
            for char in svc.characteristics:
                props=','.join(char.properties)
                print(f'  CHAR: {char.uuid} - {props}')
                if char.uuid in ['999c3104-4a1a-11e2-be66-96c7baccc598','0000fff1-0000-1000-8000-00805f9b34fb','0a0f','fff1']:
                    print(f'   **POSSIBLE MOTOR CONTROL**')
                if char.uuid in ['00000a0f-0000-1000-8000-00805f9b34fb','0a0f']:
                    print(f'   **POSSIBLE ACTIVATION**')

if __name__=='__main__':
    asyncio.run(dump_services())
