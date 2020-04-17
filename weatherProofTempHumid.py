import time
import board
import busio
import adafruit_sht31d
 
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)


def Temp():
    return(round(((sensor.temperature*9)/5)+32))
def Humidity():
    return(round(sensor.relative_humidity))


if __name__ == "__main__":
    while True:
        print(round((sensor.temperature*9/5)+32))
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(3)
        