# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
import time #import sleep
from gpiozero import InputDevice

def rainSens():
    no_rain = InputDevice(18)
    if not no_rain.is_active:
        return "It's raining - get the washing in!"
    else:
        return "not raining"
if __name__ == '__main__':
    while True:
        print(rainSens())
        time.sleep(3)
        
    