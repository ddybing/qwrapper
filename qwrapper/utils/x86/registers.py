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
    return (register_name, f'{register_name}=\s*' + r'\s*'.join(['([0-9a-fA-F]+)'] * number_of_blocks))


async def get_all_cpu_registers():
    qmp = QMPClient('x86')
    await qmp.connect('/tmp/qmp.socket')
    regs_output = await qmp.execute('human-monitor-command', {'command-line' : 'info registers'})

    registers = {}

    # This is a list of the registers to look for and match against. 
    # The second value is the number of hexadecimal "blocks" to match for.
    # E.g. GDT has 2, as there is both a base and a limit, separated by a space in the output from QMP.
    register_nums = [
        ('EAX', 1),
        ('EBX', 1),
        ('ECX', 1),
        ('EDX', 1),
        ('ESI', 1),
        ('EDI', 1),
        ('EBP', 1),
        ('ESP', 1),
        ('EIP', 1),
        ('EFL', 1),

        ('GDT', 2),
        ('IDT', 2),

        ('CR0', 1),
        ('CR2', 1),
        ('CR3', 1),
        ('CR4', 1),
        ('DR0', 1),
        ('DR1', 1),
        ('DR2', 1),
        ('DR3', 1),
        ('DR6', 1),
        ('DR7', 1),
        ('EFER', 1),
        
        ('FPR0', 2),
        ('FPR1', 2),
        ('FPR2', 1),
        ('FPR3', 1),
        ('FPR4', 1),
        ('FPR5', 1),
        ('FPR6', 1),
        ('FPR7', 1),

        ('XMM00', 1),
        ('XMM01', 1),
        ('XMM02', 1),
        ('XMM03', 1),
        ('XMM04', 1),
        ('XMM05', 1),
        ('XMM06', 1),
        ('XMM07', 1)

    ]

    register_patterns = []

    for register in register_nums:
        register_patterns.append(generate_register_pattern(register[0], register[1]))

    for register, pattern in register_patterns:
        match = re.search(pattern, regs_output)
        if match:
            registers[register] = [match.group(i) for i in range(1, len(match.groups())+1)]

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
