import subprocess
import os
import asyncio
import atexit
import time

from qemu.qmp import QMPClient




from abc import ABC, abstractmethod

# This class is a representation of an instance of a QEMU virtual machine. 
class QemuMachine(ABC):
    
    def __init__(self):
        self.QemuProcess = None

    def start(self):
        # This method starts the QEMU instance.
        pass

    def __del__(self):
        # This method is called when the object is deleted or goes out of scope.
        pass

    
    def cleanup(self):
        # This method cleans up the QEMU instance and frees up the resources. 
        pass

    @abstractmethod
    def get_all_registers():
         pass

