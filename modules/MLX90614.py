from machine import Pin, I2C
import os

machine = os.uname().machine
if ("KidBright32" in machine) or ("KidMotor V4" in machine):
    i2c1 = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
elif "Mbits" in machine:
    i2c1 = I2C(0, scl=Pin(21), sda=Pin(22), freq=400000)
else:
    i2c1 = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

def readTemp(reg):
    try:
        data = i2c1.readfrom_mem(0x5A, reg, 3)
        data = (data[1] << 8) | data[0]
        return (data * 0.02) - 273.15
    except:
        return 0

def readObjectTempC():
    return readTemp(0x07) # TOBJ1

def readAmbientTempC():
    return readTemp(0x06) # TA
