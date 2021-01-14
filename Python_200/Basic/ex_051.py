# Ex051 - Understanding class methods

class MyClass:
    def sayHello(self):
        print('Hello')

    def sayBye(self, name):
        print('%s! See you again!' %name)

obj = MyClass()
obj.sayHello()  # 'Hello' is printed out
obj.sayBye('Cheolsoo')  # 'Cheolsoo! See you again!' is printed out
