import os
disk_fd = os.open( r"\\.\PhysicalDrive1", os.O_RDONLY | os.O_BINARY)
data = os.read(disk_fd, 1024)
ascii = ""
for i, bit in enumerate(data): 
    hex_value = f'{bit:x}'.upper()
    if bit > 31 and bit < 127:
        ascii += chr(bit)
    else:
        ascii += '.'
    if len(hex_value) == 1:
        hex_value = '0' + hex_value
    print(hex_value, end=' ')
    if (i + 1) % 8 == 0: 
        if (i + 1) % 16 == 0:
            print(ascii)
            ascii = ""
        else: 
            print(" ", end='')
            
os.close(disk_fd)