#!/usr/bin/env python3
'''Records scans to a given file in the form of numpy array.
Usage example:
$ ./record_scans.py out.npy'''
import sys
from rplidar import RPLidar


PORT_NAME = '/dev/ttyUSB0' # should be 1 if running with roomba
NUMBER_BEAMS = 19 #for model

def run(path):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    outfile = open(path, 'r+')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            count = 0
            outfile.seek(0)
            outfile.truncate(0)
            line = ''
            for measurment in scan:
                if (count < NUMBER_BEAMS):
                    line = line + '\t'.join(str(v) for v in measurment)
                    line = line + '\n'
                    count = count + 1
            outfile.write(line )
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    run(sys.argv[1])
