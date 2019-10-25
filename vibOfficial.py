from gpiozero import Button
import time

vibrationSwitch = Button(17)
while True:
    if vibrationSwitch.is_pressed:
        print("button is pressed")
    else:
        print("NOT PRESSED")
        time.sleep(0.1)