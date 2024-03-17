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
        # This method is called when the object is deleted by garbage collector.
        pass

    @abstractmethod
    def cleanup(self):
        # This method cleans up the QEMU instance and frees up the resources. 
        pass

    @abstractmethod
    def get_all_registers():
         pass

class X86Machine(QemuMachine):
        def __init__(self):
            super().__init__()
            qemuCmd = ['qemu-system-i386',  '-s', '-qmp', 'unix:/tmp/qmp.socket,server=on,wait=on', '-hda', 'kernel.iso', '-hdb', 'disk.iso']
            print("Setting up virtual machine...")
            # Start Qemu with gdb stub and QMP Server. Add the kernel and disk images.
            # Virtual machine starts in "wait" mode. Waits for user to start VM execution.
            self.QemuProcess = subprocess.Popen(qemuCmd)
            atexit.register(self.cleanup)

            # Wait 2 seconds to allow QEMU to create the socket file
            time.sleep(2) 
        
        def cleanup(self):
            print("Shutting down QEMU machine...")
            self.QemuProcess.terminate()
            self.QemuProcess.wait()
            print("QEMU machine has been shut down")
            
             

        # This function gets all the registers and returns a dictionary containing every register and the corresponding values.
        def get_all_registers(self):
            if self.QemuProcess is None:
                print("QEMU process has not been initialised yet.")
                return None
            
            qmp = QMPClient('tmp')
            asyncio.run(qmp.connect('/tmp/qmp.sock'))

            result = asyncio.run(qmp.execute('query-status'))

            pass
