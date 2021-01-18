# Converting decimal numbers to hexadecimal numbers (hex)

h1 = hex(97)    # h1 is a string '0x61'
h2 = hex(98)    # h2 is a string '0x62'
ret1 = h1 + h2
print(ret1)     # '0x610x62' is printed out
a = int(h1, 16)
b = int(h2, 16)
ret2 = a + b    # ret2 becomes a decimal number 195
print(hex(ret2))# '0xc3' is printed out
