from qwrapper.qemumachine import QemuMachine
from qwrapper.utils.x86 import registers
from qemu.qmp import QMPClient
import time
import os
import subprocess
import asyncio

class X86Machine(QemuMachine):
        def __init__(self):
            super().__init__()
            qemuCmd = ['qemu-system-i386', '-display', 'none', '-s', '-qmp', 'unix:/tmp/qmp.socket,server=on,wait=on', '-hda', 'kernel.iso', '-hdb', 'disk.iso']
            print("Setting up virtual machine...")
            # Start Qemu with gdb stub and QMP Server. Add the kernel and disk images.
            # Virtual machine starts in "wait" mode. Waits for user to start VM execution.
            self.QemuProcess = subprocess.Popen(qemuCmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Wait 2 seconds to allow QEMU to create the socket file
            time.sleep(2) 
        
        def __del__(self):
            print("Shutting down QEMU machine...")
            self.QemuProcess.terminate()
            self.QemuProcess.wait()
            print("QEMU machine has been shut down")
            
             

        # This function gets all the registers and returns a dictionary containing every register and the corresponding values.
        def get_all_registers(self):
            if self.QemuProcess.poll is None:
                print("QEMU process has not been initialised yet.")
                return None
            regs = asyncio.run(registers.get_all_cpu_registers())
            return regs

