import asyncio
from bleak import BleakScanner

async def scan():
    print("Scanning FOREO BEAR...")
    devices = await BleakScanner.discover(10)
    print(f"Found {len(devices)} devices")
    for d in devices:
        name = d.name or "Unknown"
        if "FOREO" in name.upper() or "BEAR" in name.upper():
            print(f"FOUND FOREO: {d.name} - {d.address}")
            return d
    print("No FOREO device found")
    return None

asyncio.run(scan())