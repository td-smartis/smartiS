from abc import ABC, abstractmethod
 
class DataExchange(ABC):
    
    def __init__(self):
        pass

        
    def __del__(self):
        pass
    
    @abstractmethod
    def sendInformation(self):
        pass
    
    @abstractmethod
    def getInformation(self):
        pass
    

       
