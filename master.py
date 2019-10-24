import raindrp as rain
import bmeSens as BME
import uvSens as uvs
import time


class Master:
    def __init__(self, runTime):
        self.runTime = runTime
    def run(self):
        while True:
            print("Rain sensor Value: "+ str(rain.rainSens()))
            print(str(BME.BMESens1()))
            print(str(BME.BMESens2()))
            print(str(BME.BMESens3()))
            print("UV A: ", uvs.uvaVal())
            print("UV B: ", uvs.uvbVal())
            print("UV Index: ", uvs.uviVal())
            
            time.sleep(self.runTime)
obj1 = Master(3)
obj1.run()
        