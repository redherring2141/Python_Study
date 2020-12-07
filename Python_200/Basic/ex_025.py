bit1 = 0x61
bit2 = 0x62
print(hex(bit1 & bit2)) # 0x60 is printed out.
print(hex(bit1 | bit2)) # 0x63 is printed out.
print(hex(bit1 ^ bit2)) # 0x3 is printed out.
print(hex(bit1 >> 1))   # 0x30 is printed out.
print(hex(bit1 << 2))   # 0x184 is printed out.

