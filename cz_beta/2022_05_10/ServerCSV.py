from ADataExchange import *
from datetime import datetime
import csv
 
class ServerCSV(ADataExchange):
    
    def __init__(self):
        self.cvsFileName = 'serverData.csv'
        
    
    def sendInformation(self,sessionID,smartis,arguments,buttonTime,button,value):
        try:
            #print(sessionID,smartis,arguments,buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),button,value)
            data = [str(sessionID),str(smartis),str(arguments),buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),str(button),str(value)]
            with open(self.cvsFileName, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
        except:
            print("Error: Server not available")
        
    def parseToName(self,smartis, arg):  
        smartisName = smartis+"-"+arg
        return smartisName
    
    def getAllSmartisNames(self):
        dataList = []
        reader = csv.reader(open(self.cvsFileName))
        
        for raw in reader:   
            tmpRaw = self.parseToName(raw[1], raw[2])
            if not tmpRaw in dataList:
                dataList.append(tmpRaw)
                
        return dataList
    
    def getSessionIDofSmartis(self,smartisName):

        dataList = []
        reader = csv.reader(open(self.cvsFileName))
        
        for raw in reader:  
            tmpRaw = self.parseToName(raw[1], raw[2])
            if tmpRaw == smartisName:
                if not dataList:
                    dataList.append(raw[0])
                    i=0
                else:
                    if dataList[i]!= raw[0]:
                        dataList.append(raw[0])
                        i+=1
                    
        return dataList
    
    
    def getSession(self,smartisName,sessionID):
        dataList = []        
        reader = csv.reader(open(self.cvsFileName))

        for raw in reader:     
            tmpRaw = self.parseToName(raw[1], raw[2])
            if tmpRaw == smartisName and raw[0]==sessionID:
                dataList.append(raw)
                                 
        return dataList
        

    
    def clearFile(self):
        # opening the file with w+ mode truncates the file
        f = open(self.cvsFileName, "w+")
        f.close()
        
        
  
       
        



