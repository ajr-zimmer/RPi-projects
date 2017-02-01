#!/usr/bin/python
 
import spidev
import time

#Define Variables
delay = 0.5
ldr_channel = 0
force1_channel = 1
force2_channel = 2

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
    
 
while True:
    ldr_value = readadc(ldr_channel)
    force1_value = readadc(force1_channel)
    force2_value = readadc(force2_channel)
    print "---------------------------------------"
    print("LDR Value: %d" % ldr_value)
    print("Force 1 Value: %d" % force1_value)
    print("Force 2 Value: %d" % force2_value)
    time.sleep(delay)
