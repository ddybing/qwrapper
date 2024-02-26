


from qemu.qmp import QMPClient
import pygdbmi

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

    def stop():
        # This method stops the QEMU instance, without deleting it or freeing up resources.
        pass

    @abstractmethod
    def get_single_register(self, register):
        # This method gets the value of a single register from the QEMU instance.
        pass

    @abstractmethod
    def get_all_registers(self):
        # This method gets the value of all registers from the QEMU instance.
        pass

class X86Machine:
    pass

class PPCMachine:
    pass

class M68KMachine:
    pass