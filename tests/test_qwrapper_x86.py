from qwrapper import X86Machine
import time
from pygdbmi import gdbcontroller

# Create a machine
def test_x86machine_start():
    machine = X86Machine()




# Create machine and read memory
def test_x86_machine_memory():
    machine = X86Machine()

    memory = machine.read_memory_bytes(0x0, 100)

    assert memory is not None

# Create machine and add disk files
def test_x86machine_diskimages():
    machine = X86Machine(['tests/disk.iso', 'tests/disk2.iso'], False)


    # Check if the machine boots the disk images.
    # Should say 'Hello World' on screen after 10 seconds.
    VGA_MEMORY = [
    '0x48', '0x07', '0x65', '0x07', '0x6c', '0x07', '0x6c', '0x07',
    '0x6f', '0x07', '0x20', '0x07', '0x57', '0x07', '0x6f', '0x07',
    '0x72', '0x07', '0x6c', '0x07', '0x64', '0x07']

    machine.start()
    screen_memory = machine.read_memory_bytes(0xB8000, 22)

    assert screen_memory == VGA_MEMORY
