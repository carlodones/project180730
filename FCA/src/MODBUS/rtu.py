#!/usr/bin/env python
import minimalmodbus

print "WTF!"

port = '/dev/ttyUSB0'
instrument = minimalmodbus.Instrument(port, 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 57600
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
instrument.debug = True
instrument.mode = minimalmodbus.MODE_RTU
print instrument

wind_speed = instrument.read_float(1, functioncode=3,numberOfRegisters=4)
print "Wind Speed ", wind_speed