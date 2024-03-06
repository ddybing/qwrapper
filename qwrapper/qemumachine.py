
from abc import ABC, abstractmethod


# Methods that are common to all QEMU machines. 
# Methods marked with "@abstractmethod" are abstract methods, and must be implemented by the subclasses.

class QemuMachine(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    def __del__(self):
        # This method is called when the object is deleted by garbage collector.
        pass

    def cleanup(self):
        # This method cleans up the QEMU instance and frees up the resources. 
        pass

class X86Machine:
    pass