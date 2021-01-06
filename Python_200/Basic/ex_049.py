class MyClass:
    var = 'Hello'
    def sayHello(self):
        print(self.var)

obj = MyClass() # Create MyClass instance object
print(obj.var)  # 'Hello' is printed out
obj.sayHello()  # 'Hello' is printed out
