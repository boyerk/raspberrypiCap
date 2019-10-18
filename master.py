import raindrp as rain
import _testtSens as BME
import time


class Master:
    def __init__(self, runTime):
        self.runTime = runTime
    def run(self):
        while True:
            print("Rain sensor Value: "+ str(rain.rainSens()))
            print("BME280 Values: "+ str(BME.BMESens()))
            time.sleep(self.runTime)
obj1 = Master(3)
obj1.run()
        