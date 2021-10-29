from abc import ABC, abstractmethod
import time, threading
from ServerCSV import ServerCSV as Server
from datetime import datetime, timedelta
from IPython.display import clear_output
from uuid import uuid4
 
class ASmartis(ABC):
    
    def __init__(self,parameterList):
        
        self.arguments = parameterList          
        
        self.server = Server()
        self.sessionID = uuid4()
        self.sendInformationFlag = True
        
        self.thread = None
        self.updateTime = 0.05
        
        self.buttonsObject = None
        self.buttonStatesDict = {}
        self.oldButtonStatesDict = {}
        self.createButtons()
        
        self.layers = []
        self.chartWidth = 0
        self.chartHeight = 0
        self.chartObject = None
        self.createChart() 
        

    @abstractmethod
    def createButtons(self):
        pass
    
    @abstractmethod
    def createChart(self):
        pass
    
    @abstractmethod
    def visualize(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    def start(self):        
        self.thread = threading.Timer(self.updateTime, self.start)
        self.thread.start()
        smarti = str(type(self)).replace("<class '__main__.", "")
        smarti = smarti.replace("'>", "") 
        threadTime = datetime.now()
        
        if self.sendInformationFlag:
            for key in self.buttonStatesDict:
                if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                    self.server.sendInformation(self.sessionID,smarti,self.arguments,threadTime,key,self.buttonStatesDict[key])   
        
        self.update()
        
        for key in self.buttonStatesDict:
            if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                self.oldButtonStatesDict[key] = self.buttonStatesDict[key]
        

    def handleButtonEvents(self, key, value):
        self.buttonStatesDict[key] = value
      
    def stop(self):
        self.thread.cancel()
        
    def stopSendInformation(self):
        self.sendInformationFlag = False
        
    def getButtonObject(self):
        return self.buttonsObject
        
        
       
