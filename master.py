import raindropExpand as rain
import bmeSens as BME
import weatherProofTempHumid as TempAndHumidity
import uvSens as uvs
import vibExpanded as vib
import time


class Master:
    def __init__(self, runTime):
        self.runTime = runTime
    def normie(self, x, min, max):
        self.x = x
        self.min = min
        self.max = max
        y = (x - min) / (max - min)
        return round(y, 2)
    def run(self):
        counter = 0
        windCount = 0
        while True:
            counter += 1
            
            if vib.VibrationDetected() == True:
                print("WIND DETECTED!")
                windCount += 1
            #print(counter) use counter % 100 for tresting sensors % 600 for real
            if counter % 100 == 0:
                print("Rain sensor Value: "+ str(rain.rainSens()))
                file = open("/home/pi/Desktop/Sketches/sketchFinalBeforeCleanUp/data/testing.txt", "w")
                file.write(str(Master(0).normie(TempAndHumidity.Temp(), 50, 101)))
                file.write("\n" + str(Master(0).normie(TempAndHumidity.Humidity(), 10, 80)))
                file.write("\n" + str(Master(0).normie(BME.BMESens3(), 970, 1030)))
                file.write("\n" + str(rain.rainSens()))
                if windCount >= 10:
                    file.write("\n" + "1")
                else:
                    file.write("\n" + "0")
                file.write("\n" + str(Master(0).normie(uvs.uviVal(), 0, 11)))
                file.close()
                print(str(TempAndHumidity.Temp()))
                print(str(TempAndHumidity.Humidity()))
                print(str(BME.BMESens3()))
                print(str(windCount))
                print("UV A: ", uvs.uvaVal())
                print("UV B: ", uvs.uvbVal())
                print("UV Index: ", uvs.uviVal())
                print(str(counter))
                counter = 0
                windCount = 0
                
            time.sleep(self.runTime)
            
if __name__ == "__main__":
    MasterFile = Master(0.15)
    #MasterFile = Master(0.03) TIME FOR TESTING
    MasterFile.run()
        