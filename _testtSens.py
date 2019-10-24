import board
import busio
import adafruit_bme280



def BMESens():
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    T = bme280.temperature
    H = bme280.humidity
    P = bme280.pressure
    
    return (T,H,P)