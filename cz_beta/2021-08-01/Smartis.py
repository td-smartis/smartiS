from ISmartis import *
from abc import ABC, abstractmethod
import time, threading
from ServerSQL import *
from datetime import datetime, timedelta
 
class Smartis(ISmartis, ABC):
    
    def __init__(self):
        print("KonstruktorS")
        self.server = ServerSQL()
        self.updateTime = 0.05
        self.buttonStatesDict = {}
        self.oldButtonStatesDict = {}
        
        self.createButtons()
        self.createChart() 

        
    def __del__(self):
        self.stop()
        print("deleteS")
    
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
        sessionID = "1234"
        smarti = str(type(self)).replace("<class '__main__.", "")
        smarti = smarti.replace("'>", "") 
        threadTime = datetime.now()
        
        for key in self.buttonStatesDict:
            if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                self.server.sendInformation(sessionID,smarti,threadTime,key,self.buttonStatesDict[key])   
        
        self.update()
        
        for key in self.buttonStatesDict:
            if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                self.oldButtonStatesDict[key] = self.buttonStatesDict[key]
        
        
        
        '''
        changesDict = {}
        for key in self.buttonStatesDict:
            if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                changesDict[key] =  self.buttonStatesDict[key]       
        
        self.update()
        
        for key in self.buttonStatesDict:
            if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                changesDict[key] =  self.buttonStatesDict[key] 
                self.oldButtonStatesDict[key] = self.buttonStatesDict[key]
                
        for key in changesDict:
            self.server.sendInformation(sessionID,smarti,threadTime,key,changesDict[key])
            '''
        
    def handleButtonEvents(self, key, value):
        self.buttonStatesDict[key] = value
        #print(self.buttonStatesDict)
        #print(self.oldButtonStatesDict)

        
        
    def stop(self):
        self.thread.cancel()
        
    def stopSendInformation(self):
        self.server.setSendFlag(False)
        
    def getButtonObject(self):
        return self.buttonsObject
        
        
       
