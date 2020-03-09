"""
    Go and  back example with roomba
"""
from time import sleep
import sys
import numpy as np
from time import sleep
from pyroombaadapter import PyRoombaAdapter

def read_flag(path):
	try:
		outfile = open(path, 'r')
	except IOError:
		read_flag(path)
	with outfile:
		s = outfile.readlines()
		outfile.close()	
		#s = s[0].split("\n")
		print(s)
		if (s == []):
		 return 0
		return float(s[0])

def write_flag(path):
	try:
		outfile = open(path, 'r+')
	except IOError:
		read_lidar(path)
	with outfile:
		outfile.seek(0)
		outfile.truncate(0)
		outfile.write(str(0))
		outfile.close()	

PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)
while(1):
	flag = read_flag(sys.argv[1])
	if (flag != 0):	
		adapter.move(0, flag)  # turn right
		sleep(0.2)
	adapter.move(0.2, np.deg2rad(0.0))  # go straight
	write_flag(sys.argv[1])


