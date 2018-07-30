#!/usr/bin/env python
import minimalmodbus

import time



minimalmodbus.BAUDRATE = 57600

# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

#while True:
# Register number, number of decimals, function code
temperature = instrument.read_registers(0, 10, 3)
print temperature
time.sleep(1)
    