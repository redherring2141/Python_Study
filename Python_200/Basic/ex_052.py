# Ex052 - Understanding class constructor

class MyClass:
    def __init__(self):
        self.var = 'Hello!'
        print('MyClass instance object is generated')

obj = MyClass()     # 'MyClass instance object is generated' is printed out
print(obj.var)      # 'Hello' is printed out
