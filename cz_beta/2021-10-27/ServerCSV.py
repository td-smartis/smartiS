from ADataExchange import *
from datetime import datetime
import csv
 
class ServerCSV(ADataExchange):
    
    def __init__(self):
        self.cvsFileName = 'serverData.csv'
        
    
    def sendInformation(self,sessionID,smarti,arguments,buttonTime,button,value):
        
        #print(sessionID,smarti,arguments,buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),button,value)
        data = [str(sessionID),str(smarti),str(arguments),buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),str(button),str(value)]
        with open(self.cvsFileName, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        
    def parseToName(self,smarti, arg):  
        smartiName = smarti+"-"+arg
        return smartiName
    
    def getAllSmartiNames(self):
        dataArray = []
        reader = csv.reader(open(self.cvsFileName))
        
        for raw in reader:   
            tmpRaw = self.parseToName(raw[1], raw[2])
            if not tmpRaw in dataArray:
                dataArray.append(tmpRaw)
                
        return dataArray
    
    def getSessionIDofSmarti(self,smartiName):

        dataArray = []
        reader = csv.reader(open(self.cvsFileName))
        
        for raw in reader:  
            tmpRaw = self.parseToName(raw[1], raw[2])
            if tmpRaw == smartiName:
                if not dataArray:
                    dataArray.append(raw[0])
                    i=0
                else:
                    if dataArray[i]!= raw[0]:
                        dataArray.append(raw[0])
                        i+=1
                    
        return dataArray
    
    
    def getSession(self,smartiName,sessionID):
        dataArray = []
        sessionArray = []
        
        reader = csv.reader(open(self.cvsFileName))

        for raw in reader:     
            tmpRaw = self.parseToName(raw[1], raw[2])
            if tmpRaw == smartiName and raw[0]==sessionID:
                dataArray.append(raw)
                                 
        return dataArray
        

    
    def clearFile(self):
        # opening the file with w+ mode truncates the file
        f = open(self.cvsFileName, "w+")
        f.close()
        
        
  
       
        



