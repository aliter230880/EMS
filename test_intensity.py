import asyncio
from bleak import BleakClient, BleakScanner

DEVICE_MAC='A4:34:F1:AB:D9:7C'
SERIAL='eZxQX43wHKg2tJ'
ACTIVATE_UUID='00000a0f-0000-1000-8000-00805f9b34fb'
MOTOR_UUID='0000fff1-0000-1000-8000-00805f9b34fb'

async def activate_device(client):
    token=SERIAL.encode('ascii')
    try:
        await client.write_gatt_char(ACTIVATE_UUID,token,response=False)
        print('Activation token sent!')
        return True
    except Exception as e:
        print(f'Activation failed: {e}')
        return False

async def send_ems_command(client,intensity,mode):
    command=bytearray([100,intensity,mode,128])
    try:
        await client.write_gatt_char(MOTOR_UUID,command,response=False)
        print(f'OK: intensity={intensity}, mode={mode}')
        return True
    except Exception as e:
        print(f'ERROR: {e}')
        return False

async def intensity_test():
    print('FOREO BEAR Intensity Test')
    print('Searching device...')
    device=await BleakScanner.find_device_by_address(DEVICE_MAC,timeout=15.0)
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
        print('Sending activation token...')
        if not await activate_device(client):
            return
        await asyncio.sleep(0.5)
        print('='*60)
        print('PUT DEVICE ON YOUR SKIN NOW!')
        print('Testing intensities 1-15 (Mode 1: Anti-Aging)')
        print('Each intensity will run for 3 seconds')
        print('='*60)
        input('Press ENTER when ready...')
        for i in range(1,16):
            print(f'\nINTENSITY {i}/15')
            await send_ems_command(client,i,1)
            await asyncio.sleep(3)
        print('\nStopping...')
        await send_ems_command(client,0,1)
        print('Test done!')

if __name__=='__main__':
    asyncio.run(intensity_test())
