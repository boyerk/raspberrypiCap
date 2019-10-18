import time
from Adafruit_BME280 import *

def BMESens():
    bme = BME280(t_mode=BME280_OSAMPLE_8,h_mode=BME280_OSAMPLE_8,p_mode=BME280_OSAMPLE_8)
    T,H,P = (None, None, None)


    T = bme.read_temperature()
    H = bme.read_humidity()
    P = bme.read_pressure()
    return (T,H,P)
        