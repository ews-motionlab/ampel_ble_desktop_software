
import logging
logging.basicConfig(level=logging.WARNING)			# enable debug messages
import time

import bluetooth

import asyncio
import platform                                     # detecting if windows or linux
from bleak import BleakScanner
from bleak import BleakClient

class ble_device():

    client = None                                  # used for dealing with Bleak
    mac_addr = None                                # ble address
    services = None

    def __init__(self):
        pass

    def read_charac(self):
        pass

    def write_charac(self):
        pass

    def read_desc(self):
        pass

    def write_desc(self):           # is that needed ???
        pass

    def connect(self,addr = None):
        logging.debug("connect() method called")
        if addr is not None:                         # optional, if address already assigned
            self.addr = mac_addr
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run_connect(self.mac_addr))

    async def run_connect(self,addr):
        client = BleakClient(addr)
        try:
            await client.connect()
        except Exception as e:
            print(e)
        finally:
            await client.disconnect()

    def get_ble_devices(self):
        #logging.debug("get_ble_devices() method called")
        devices = []
        loop = asyncio.get_event_loop()
        devices = loop.run_until_complete(self.run_scan())
        return(devices)

    async def run_scan(self):
        logging.debug("BLE Devices")
        devices = await BleakScanner.discover()
        return(devices)

    def get_services(self):

        # mac_addr = (
        #     "80:7D:3A:BA:13:D6"
        #     if platform.system() != "Darwin"
        #     else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
        # )
        loop = asyncio.get_event_loop()
        self.services = loop.run_until_complete(self.run_get_services(self.mac_addr))

        print("SERVICES inside ble_device.get_services() method")
        for service in self.services:
            print(service)

        return(self.services)

    async def run_get_services(self,mac_addr: str):
        #async with BleakClient(mac_addr) as client:
        async with self.client as client:
            svcs = await client.get_services()
            time.sleep(0.01)
            return svcs

    def set_mac_addr(self, addr):
        self.mac_addr = addr
        self.client = BleakClient(self.mac_addr)


if __name__ == "__main__":
    device = ble_device()
    devs = device.get_ble_devices()

    mac_addr = None

    for d in devs:
        print(d)

    for d in devs:
        if d.name == "AmpelBLE":      # device name
            mac = d.address           # this is extremelly unelegant, find better way

    print("mac address")
    print(mac)
    device.set_mac_addr(mac)
    device.connect()
    services = device.get_services()
    print(services)


