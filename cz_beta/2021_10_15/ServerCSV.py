from DataExchange import *
from datetime import datetime
import csv
 
class ServerCSV(DataExchange):
    
    def __init__(self):
        pass
        

        
    def __del__(self):
        pass
    
    def sendInformation(sessionID,smarti,arguments,buttonTime,button,value):
        
        print(sessionID,smarti,arguments,buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),button,value)
        data = [str(sessionID),str(smarti),str(arguments),buttonTime.strftime("%m/%d/%Y, %H:%M:%S.%f"),str(button),str(value)]
        with open('serverData.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        
    def parseToName(smarti, arg):  
        smartiName = smarti+"-"+arg
        return smartiName
    
    def getAllSmartiNames():
        dataArray = []
        reader = csv.reader(open("serverdata.csv"))
        
        for raw in reader:   
            tmpRaw = ServerCSV.parseToName(raw[1], raw[2])
            if not tmpRaw in dataArray:
                dataArray.append(tmpRaw)
                
        return dataArray
    
    def getUserIDofSmarti(smarti):

        dataArray = []
        reader = csv.reader(open("serverdata.csv"))
        i = -1
        for raw in reader:  
            tmpRaw = ServerCSV.parseToName(raw[1], raw[2])
            if tmpRaw == smarti:
                if i<0:
                    dataArray.append(raw[0])
                    i+=1
                elif i>-1 and dataArray[i-1]!= raw[0]:
                    dataArray.append(raw[0])
                    i+=1
        return dataArray
    
    def getSession(smartiName,sessionID):
        dataArray = []
        sessionArray = []
        
        reader = csv.reader(open("serverdata.csv"))

        for raw in reader:     
            tmpRaw = ServerCSV.parseToName(raw[1], raw[2])
            if tmpRaw == smartiName and raw[0]==sessionID and raw[3]!= "b_reset":
                sessionArray.append(raw)
                
            elif tmpRaw == smartiName and raw[0]==sessionID and raw[3]== "b_reset":
                sessionArray.append(raw)
                dataArray.append(sessionArray.copy())
                sessionArray.clear()
                
        dataArray.append(sessionArray.copy())
        return dataArray
        

    
    def clearFile():
        filename = "serverData.csv"
        # opening the file with w+ mode truncates the file
        f = open(filename, "w+")
        f.close()
        
        
  
       
        



