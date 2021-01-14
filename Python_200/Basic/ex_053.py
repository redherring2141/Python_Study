# Ex053 - Understanding class destructor

class MyClass:
    def __del__(self):
        print('MyClass instance object is removed from memory')

obj = MyClass()
del obj     # 'MyClass instance object is removed from memory' is printed out
