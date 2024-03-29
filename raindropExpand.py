import board
import busio
import digitalio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

def rainSens():
    raindrop = mcp.get_pin(9)
    raindrop.direction = digitalio.Direction.INPUT
    if raindrop.value == False:
        return 1
    else:
        return 0
if __name__ == '__main__':
    while True:
        print(rainSens())
        time.sleep(3)
