
import logging
logging.basicConfig(level=logging.DEBUG)			# enable debug messages

from ble_ampel import *                             # custom class created for the ble ampel

import bluetooth

import asyncio
from bleak import BleakScanner
from bleak import BleakClient


# GLOBAL VARIABLES #
address = "80:7D:3A:BA:13:D6"
MODEL_NBR_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"

if __name__ == '__main__':
    ampel = ble_ampel()



#
# if __name__ == '__main__':
#
#     async def run_scan():
#         logging.debug("BLE Devices")
#         devices = await BleakScanner.discover()
#         return(devices)
#
#     def get_ble_devices():
#         devices = []
#         loop = asyncio.get_event_loop()
#         devices = loop.run_until_complete(run_scan())
#         return(devices)
#
#     def ble_connect(addr):
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(run_connect(addr))
#
#     async def run_connect(addr):
#         client = BleakClient(addr)
#         try:
#             await client.connect()
#             led_descriptor = await client.read_gatt_char("beb5482e-36e1-4688-b7f5-ea07361b26a8")
#             await client.write_gatt_char("beb5482e-36e1-4688-b7f5-ea07361b26a8",b'3')
#             print("buttons: {0}".format("".join(map(chr, led_descriptor))))
#             # await client.write_gatt_char("beb5482e-36e1-4688-b7f5-ea07361b26a8",b'0')
#             # print("buttons: {0}".format("".join(map(chr, led_descriptor))))
#
#             #model_number = await client.read_gatt_char(MODEL_NBR_UUID)
#             #print("Model Number: {0}".format("".join(map(chr, model_number))))
#         except Exception as e:
#             print(e)
#         finally:
#             await client.disconnect()
#
#     ble_devices = get_ble_devices()
#     for d in ble_devices:
#         print(d)
#     ble_connect(address)
#
#     logging.debug("Everything exploded")



