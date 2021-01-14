# Ex050 - Understanding class members and instance members

class MyClass:
    var = 'Good day!!'
    def sayHello(self):
        param1 = 'Hello'
        self.param2 = 'Hi'
        print(param1)   # 'Hello' is printed out
        print(self.var) # 'Hi' is printed out

obj = MyClass()
print(obj.var)      # 'Hello' is printed out
obj.sayHello()
#obj.param1
