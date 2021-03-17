"""
Services
----------------
An example showing how to fetch all services and print them.
Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>
"""

import asyncio
import platform

from bleak import BleakClient


async def run_get_services(mac_addr: str):
    async with BleakClient(mac_addr) as client:
        svcs = await client.get_services()
        return svcs


def get_services():

    mac_addr = (
        "80:7D:3A:BA:13:D6"
        if platform.system() != "Darwin"
        else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
    )
    loop = asyncio.get_event_loop()
    services = loop.run_until_complete(run_get_services(mac_addr))

    for service in services:
        print(service)

    return(services)

services = get_services()
for s in services:
    print(s)