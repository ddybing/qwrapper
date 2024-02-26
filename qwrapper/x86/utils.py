

multiboot2= 0xE85250D6


def search_multiboot_magic(file):
    magic_bytes_le = multiboot2.to_bytes(4, byteorder='little')
    magic_bytes_be = multiboot2.to_bytes(4, byteorder='big')