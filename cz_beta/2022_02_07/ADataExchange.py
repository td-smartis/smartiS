from abc import ABC, abstractmethod
 
class ADataExchange(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def sendInformation(self,sessionID,smartis,arguments,buttonTime,button,value):
        pass

    @abstractmethod
    def getAllSmartisNames(self):
        pass
    
    @abstractmethod
    def getSessionIDofSmartis(self,smartisName):
        pass
    
    @abstractmethod
    def getSession(self,smartisName,sessionID):
        pass