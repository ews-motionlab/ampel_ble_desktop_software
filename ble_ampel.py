
import logging
logging.basicConfig(level=logging.DEBUG)			# enable debug messages
from ble_device import *                            # class where the ble device from which ble_ample inherits

import bluetooth

import asyncio
from bleak import BleakScanner
from bleak import BleakClient

class ble_ampel(ble_device):

    def __init__(self):
        super().__init__()                          # initialization of the underlying  class (ble_device)


    def connect(self):
        pass
        # do bleak stuff to establish a pseudo-conection with the remote device
        #SUPER.CONNECT
    def get_leds_status(self):
        pass

    def set_leds_status(self):
        pass

    def get_buttons_status(self):                         # the amel has some buttons, which can be user triggered (no SET method for this)
        pass

if __name__ == "__main__":
    pass