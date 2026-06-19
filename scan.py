import asyncio
from bleak import BleakScanner

async def scan():
d=await BleakScanner.discover(10)
for x in d:
if x.name and (\" "FOREO\ in x.name.upper() or \BEAR\ in x.name.upper()):
print(x.name,x.address)
return x

asyncio.run(scan())
