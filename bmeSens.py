import board
import time
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
T = bme280.temperature
H = bme280.humidity
P = bme280.pressure
def BMESens1():
    #return("Temperature: %0.1f C" % T)
    return(round((T*9/5)+32))
def BMESens2():
    #return("Humidity: %0.1f %%" % H)
    return(round(H))
def BMESens3():
    #return("Pressure: %0.1f hPa" % P)
    return(round(P))
if __name__ == "__main__":
    while True:
        print(BMESens1())
        print(BMESens2())
        print(BMESens3())
        time.sleep(3)