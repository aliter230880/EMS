import asyncio
from bleak import BleakClient, BleakScanner

BEAR_MAC = "A4:34:F1:AB:D9:7C"
SERIAL_NUMBER = "eZxQX43wHKg2tJ"
ACTIVATE_UUID = "00000a0f-0000-1000-8000-00805f9b34fb"

async def main():
    print("[1] Scanning for BEAR...")
    device = await BleakScanner.find_device_by_address(BEAR_MAC, timeout=10.0)
    if not device:
        print("[ERROR] BEAR not found. Turn ON device.")
        return
    print(f"[2] Found: {device}")
    
    async with BleakClient(device) as client:
        print("[3] Connected!")
        serial_bytes = SERIAL_NUMBER.encode("ascii")
        print(f"[4] Activating: {serial_bytes.hex()}")
        await client.write_gatt_char(ACTIVATE_UUID, serial_bytes)
        print("[5] Activation sent!")

asyncio.run(main())