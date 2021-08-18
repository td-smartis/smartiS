from DataExchange import *
from datetime import datetime
import csv
 
class ServerSQL(DataExchange):
    
    def __init__(self):
        self.sendFlag = True 
        pass

        
    def __del__(self):
        pass
    
    def sendInformation(self,sessionID,smarti,buttonTime,button,value):
        if self.sendFlag:
            print(sessionID,smarti,buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),button,value)
            data = [str(sessionID),str(smarti),buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),str(button),str(value)]
            with open('SmartisData.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
        
    
    def getInformation(self):
        dataArray = []
        reader = csv.reader(open("SmartisData.csv"))
        for raw in reader:
            #print(raw)
            dataArray.append(raw)
        return dataArray
    def setSendFlag(self,value):
        self.sendFlag = value
       
        



