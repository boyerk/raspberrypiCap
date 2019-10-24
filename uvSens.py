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
if __name__ == "__main__":
    while True:
        print("UV A: ", uvaVal())
        print("UV B: ", uvbVal())
        print("UV Index: ", uviVal())
        time.sleep(3)

