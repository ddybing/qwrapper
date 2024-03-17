# This module helps to read the CPU registers of the QEMU machine
# and return them in a structured format.

from qemu.qmp import QMPClient 
import re

async def get_all_cpu_registers_raw():
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    regs_output = await qmp.execute('human-monitor-command', {'command-line' : 'info registers'})
    return regs_output


def generate_register_pattern(register_name, number_of_blocks):
    return (register_name, f'{register_name}=' + r'\s*'.join(['([0-9a-fA-F]+)'] * number_of_blocks))


async def get_all_cpu_registers():
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    regs_output = await qmp.execute('human-monitor-command', {'command-line' : 'info registers'})

    registers = {}

    register_patterns = [
        ('EAX', 'EAX=([0-9a-fA-F]+)'),
        ('EBX', 'EBX=([0-9a-fA-F]+)'),
        ('ECX', 'ECX=([0-9a-fA-F]+)'),
        ('EDX', 'EDX=([0-9a-fA-F]+)'),
        ('ESI', 'ESI=([0-9a-fA-F]+)'),
        ('EDI', 'EDI=([0-9a-fA-F]+)'),
        ('EBP', 'EBP=([0-9a-fA-F]+)'),
        ('ESP', 'ESP=([0-9a-fA-F]+)'),
        ('EIP', 'EIP=([0-9a-fA-F]+)'),
        ('EFL', 'EFL=([0-9a-fA-F]+)'),

        ('GDT', r'GDT=\s*([0-9a-fA-F]+)\s+([0-9a-fA-F]+)'),
        ('IDT', r'GDT=\s*([0-9a-fA-F]+)\s+([0-9a-fA-F]+)'),

        ('CR0', 'CR0=([0-9a-fA-F]+)'),


    ]

    two_value_registers = ['GDT', 'IDT']
    for register, pattern in register_patterns:
        match = re.search(pattern, regs_output)
        if match:
            if register in two_value_registers:
                registers[register] = [match.group(1), match.group(2)]
            else:
                registers[register] = match.group(1)

    print(regs_output)
    print(registers['CR0'])
    return registers

async def get_register(requested_register):
    registers = await get_all_cpu_registers




    if requested_register in registers:
        return registers[requested_register]
    else:
        return None



async def get_gdt_register():
    """
    Returns the contents of the GDT register in the form of an array with base and limit.
    
    This function retrieves the GDT register value by parsing the raw CPU registers.
    It searches for the GDT value using a regular expression and extracts the base and limit values.
    The base and limit values are then stored in an array and returned.
    """
    all_registers = await get_all_cpu_registers_raw()

    # GDT pointer, first value is base, second is limit.
    gdtptr = [0x0, 0x0]
    match = re.search(r'GDT=\s*([0-9a-fA-F]+)\s*([0-9a-fA-F]+)', all_registers)
    if match:
        gdt_value1 = int(match.group(1), 16)
        gdt_value2 = int(match.group(2), 16)
        gdtptr[0] = gdt_value1
        gdtptr[1] = gdt_value2

    return gdtptr
