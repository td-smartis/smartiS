from abc import ABC, abstractmethod
import time, threading
from ServerCSV import ServerCSV as Server
from Buttons import *   
from Chart import *
from datetime import datetime, timedelta
from IPython.display import clear_output
from uuid import uuid4
from IPython.display import HTML
 
class ASmartis(ABC):
    
    def __init__(self,parameterList):
        
        display(HTML("<style>.jp-OutputArea-output { width: 90% !important; }</style>"))
        
        self.arguments = parameterList          
        
        self.server = Server()
        self.sessionID = uuid4()
        self.sendInformationFlag = True
        
        self.updateTime = 0.05
        
        self.buttonsObject = None
        self.buttonsStatesDict = {}
        self.oldButtonsStatesDict = {}
        
        self.createButtons()

        self.createChart() 
        
    def __del__(self):
        print("delete")
        self.stop()
        

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
    
    @abstractmethod
    def reset(self):
        pass
    
    def start(self):        
        self.thread = threading.Timer(self.updateTime, self.start)
        self.thread.start()
        smartis = str(type(self)).replace("<class '__main__.", "")
        smartis = smartis.replace("'>", "") 
        threadTime = datetime.now()
        
        if self.sendInformationFlag:
            for key in self.buttonsStatesDict:
                if self.buttonsStatesDict[key] != self.oldButtonsStatesDict[key]:
                    self.server.sendInformation(self.sessionID,smartis,self.arguments,threadTime,key,self.buttonsStatesDict[key])   
        
        self.update()
        
        for key in self.buttonsStatesDict:
            if self.buttonsStatesDict[key] != self.oldButtonsStatesDict[key]:
                self.oldButtonsStatesDict[key] = self.buttonsStatesDict[key]
        

    def handleButtonEvents(self, key, value):
        self.buttonsStatesDict[key] = value
      
    def stop(self):
        self.thread.cancel()
        del self.thread
        
    def stopSendInformation(self,flag = False):
        self.sendInformationFlag = flag
        
    def getButtonsObject(self):
        return self.buttonsObject
        
        
       
