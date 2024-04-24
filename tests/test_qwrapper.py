from qwrapper.x86 import X86Machine

# Create a machine
def test_x86machine():
    machine = X86Machine()


# Create machine and read memory
def test_x86_machine():
    machine = X86Machine()
    memory = machine.read_memory_bytes(0x0, 100)
    assert memory is not None
