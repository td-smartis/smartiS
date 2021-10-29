from abc import ABC, abstractmethod
 
class ADataExchange(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def sendInformation(self,sessionID,smarti,arguments,buttonTime,button,value):
        pass

    @abstractmethod
    def getAllSmartiNames(self):
        pass
    
    @abstractmethod
    def getSessionIDofSmarti(self,smartiName):
        pass
    
    @abstractmethod
    def getSession(self,smartiName,sessionID):
        pass