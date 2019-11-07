import board
import busio
import digitalio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

pin8 = mcp.get_pin(8)
pin8.direction = digitalio.Direction.INPUT
pin8.pull = digitalio.Pull.UP
pin9 = mcp.get_pin(9)
pin9.direction = digitalio.Direction.INPUT
#pin9.pull = digitalio.Pull.UP
while True:
    print(pin9.value)
    time.sleep(0.1)
    