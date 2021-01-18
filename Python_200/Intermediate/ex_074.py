# Ex074 - Extracting upper 4 bits from 1 byte

a = 107
b = (a>>4) & 0x0f
print(b)    # 6 is printed out
