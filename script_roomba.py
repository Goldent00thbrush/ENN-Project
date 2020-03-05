"""
    Go and  back example with roomba
"""
from time import sleep

import numpy as np
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)
while(1):
	adapter.move(0.2, np.deg2rad(0.0))  # go straight

