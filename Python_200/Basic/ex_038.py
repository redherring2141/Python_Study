dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a'])   # 1 is printed out
dict1['d'] = 4
print(dict1)        # {'a':1, 'b':2, 'c':3, 'd':4} is printed out, but the order might be different.
dict1['b'] = 7
print(dict1)        # {'a':1, 'b':7, 'c':3, 'd':4} is printed out, but the order might be different.
print(len(dict1))   # 4 is printed out
