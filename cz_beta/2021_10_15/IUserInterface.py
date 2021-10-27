from abc import ABC, abstractmethod
 
class IUserInterface(ABC):
 
    @abstractmethod
    def resize(self):
        pass
