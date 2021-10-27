from abc import ABC, abstractmethod
 
class ISmartis(ABC):
 
    @abstractmethod
    def __del__(self):
        pass
    
    @abstractmethod
    def handleButtonEvents(self):
        pass
