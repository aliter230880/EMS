import asyncio
from bleak import BleakClient, BleakScanner

DEVICE_MAC='A4:34:F1:AB:D9:7C'
SERIAL='eZxQX43wHKg2tJ'
WAKE_UP_UUID='00000a0d-0000-1000-8000-00805f9b34fb'
ACTIVATE_UUID='00000a0f-0000-1000-8000-00805f9b34fb'
MOTOR_UUID='0000fff1-0000-1000-8000-00805f9b34fb'
MODES={1:'Anti-Aging',2:'Toning',3:'Spa',4:'Sculptor',5:'Massage',6:'Custom'}

async def wake_up_device(client):
    try:
        await client.write_gatt_char(WAKE_UP_UUID,bytes.fromhex('01'), response=False)
        print('Wake-up command sent!')
        return True
    except Exception as e:
        print(f'Wake-up failed: {e}')
        return False

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
        print(f'OK: intensity={intensity}, mode={mode} ({MODES.get(mode)})')
        return True
    except Exception as e:
        print(f'ERROR: {e}')
        return False

async def stop_device(client):
    return await send_ems_command(client,0,1)

async def find_device():
    print(f'Searching {DEVICE_MAC}...')
    for attempt in range(3):
        if attempt>0:
            print(f'Attempt {attempt+1}/3...')
        device=await BleakScanner.find_device_by_address(DEVICE_MAC,timeout=15.0)
        if device:
            print(f'Found: {device.name or device.address}')
            return device
        await asyncio.sleep(2)
    print('Device not found')
    return None

async def interactive_control():
    print('='*60)
    print('FOREO BEAR EMS Control')
    print('='*60)
    device=await find_device()
    if not device:
        return
    print('Connecting...')
    async with BleakClient(device,timeout=30.0) as client:
        if not client.is_connected:
            print('Connection failed')
            return
        print('Connected!')
        print('Sending wake-up command...')
        if not await wake_up_device(client):
            return
        await asyncio.sleep(0.5)
        print('Sending activation token...')
        if not await activate_device(client):
            return
        await asyncio.sleep(0.5)
        print('Modes: 1=AntiAging 2=Toning 3=Spa 4=Sculptor 5=Massage 6=Custom')
        print('Intensity: 0-15, Commands: stop, quit')
        print('Example: 5 1 = intensity 5, mode Anti-Aging')
        while True:
            try:
                cmd=input('Enter [intensity mode]: ').strip().lower()
                if cmd in ['quit','exit','q']:
                    print('Stopping...')
                    await stop_device(client)
                    break
                if cmd in ['stop','s']:
                    await stop_device(client)
                    continue
                parts=cmd.split()
                if len(parts)!=2:
                    print('Format: [intensity] [mode] - example: 5 1')
                    continue
                intensity=int(parts[0])
                mode=int(parts[1])
                if not(0<=intensity<=15) or not(1<=mode<=6):
                    print('Intensity: 0-15, Mode: 1-6')
                    continue
                await send_ems_command(client,intensity,mode)
            except KeyboardInterrupt:
                await stop_device(client)
                break
            except Exception as e:
                print(f'Error: {e}')

async def quick_test():
    print('FOREO BEAR Quick Test')
    device=await find_device()
    if not device:
        return
    print('Connecting...')
    async with BleakClient(device,timeout=30.0) as client:
        if not client.is_connected:
            print('Connection failed')
            return
        print('Connected!')
        print('Sending wake-up command...')
        if not await wake_up_device(client):
            return
        await asyncio.sleep(0.5)
        print('Sending activation token...')
        if not await activate_device(client):
            return
        await asyncio.sleep(0.5)
        print('Testing modes (intensity=5)...')
        for mode_id in range(1,7):
            print(f'Mode {mode_id}: {MODES[mode_id]}')
            await send_ems_command(client,5,mode_id)
            await asyncio.sleep(3)
        await stop_device(client)
        print('Test done!')

def main():
    print('1. Interactive control')
    print('2. Quick test')
    choice=input('Choice (1/2): ').strip()
    if choice=='2':
        asyncio.run(quick_test())
    else:
        asyncio.run(interactive_control())

if __name__=='__main__':
    main()
