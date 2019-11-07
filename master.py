import raindropExpand as rain
import bmeSens as BME
import uvSens as uvs
import vibExpanded as vib
import time


class Master:
    def __init__(self, runTime):
        self.runTime = runTime
    def run(self):
        counter = 0
        while True:
            counter += 1
            print("wind detection: ", vib.VibrationDetected())
            print(counter)
            if counter % 30 == 0:
                print("Rain sensor Value: "+ str(rain.rainSens()))
                print(str(BME.BMESens1()))
                print(str(BME.BMESens2()))
                print(str(BME.BMESens3()))
                print("UV A: ", uvs.uvaVal())
                print("UV B: ", uvs.uvbVal())
                print("UV Index: ", uvs.uviVal())
            
            time.sleep(self.runTime)
            
if __name__ == "__main__":
    MasterFile = Master(0.1)
    MasterFile.run()
        