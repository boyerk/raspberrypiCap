import board
import busio
import digitalio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)


def VibrationDetected():
    vibSwitch1 = mcp.get_pin(8)
    vibSwitch1.direction = digitalio.Direction.INPUT
    vibSwitch1.pull = digitalio.Pull.UP
    if vibSwitch1.value == False:
        return("vibration Detected!")
    else:
        return("No Shake")
    

if __name__ == '__main__':      
    while True:
        print(VibrationDetected())
        time.sleep(0.05)