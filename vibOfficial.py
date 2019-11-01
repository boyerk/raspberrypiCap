from gpiozero import Button
import time

vibrationSwitch = Button(17)

def VibrationDetected():
    
    if vibrationSwitch.is_pressed:
        return("button is pressed")
    else:
        return("NOT PRESSED")
    

if __name__ == '__main__':      
    while True:
        if vibrationSwitch.is_pressed:
            print("button is pressed")
        else:
            print("NOT PRESSED")
            time.sleep(0.1)