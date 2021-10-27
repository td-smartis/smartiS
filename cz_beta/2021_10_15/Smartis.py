from ISmartis import *
from abc import ABC, abstractmethod
import time, threading
from ServerCSV import ServerCSV as Server
from datetime import datetime, timedelta
from IPython.display import clear_output
from uuid import uuid4
 
class Smartis(ISmartis, ABC):
    
    def __init__(self,parameterList):

        self.sessionID = uuid4()
        self.arguments = parameterList
        self.updateTime = 0.05
        self.buttonStatesDict = {}
        self.oldButtonStatesDict = {}
        
        self.createButtons()
        self.createChart() 
        self.sendInformationFlag = True

        
    def __del__(self):
        #self.stop()
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
        smarti = str(type(self)).replace("<class '__main__.", "")
        smarti = smarti.replace("'>", "") 
        threadTime = datetime.now()
        
        if self.sendInformationFlag:
            for key in self.buttonStatesDict:
                if self.buttonStatesDict[key] != self.oldButtonStatesDict[key]:
                    Server.sendInformation(self.sessionID,smarti,self.arguments,threadTime,key,self.buttonStatesDict[key])   
        
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
        self.sendInformationFlag = False
        
    def stopVisualize(self):
        del self.chartObject
        
    def getButtonObject(self):
        return self.buttonsObject
        
        
       
