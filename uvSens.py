import time
import board
import busio
import adafruit_veml6075

i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

def uvaVal():
    return(veml.uva)
def uvbVal():
    return(veml.uvb)
def uviVal():
    return(veml.uv_index)

