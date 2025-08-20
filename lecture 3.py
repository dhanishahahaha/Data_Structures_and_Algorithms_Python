'''Classes and Objects

A class is a blueprint or a description of an object, it can define various attributes of an object.
Encapsulation --> Act of combining or grouping properties and methods related same object. Class is a way to implement encapsulation.
There are two types of objects in Python: instance and class objects
'''
class test:    #test is the class object
    def __init__(self,a,b):   # a and b are the local variables, self refers the same object t1 or t2 will refer
        self.a=a
        self.b=b

t1 = test(3,4)   #t1 and t2 are instance objects of class Test, when this runs the init method is called
t2 = test(7,8)
print(t1.a , t1.b)
print(t2.a , t2.b)

'''
Methods in a class:
1. Instance Method --> Needs minimum 1 arg, no decorator is needed
2. Static Method --> No number of minimum args req, decorator is needed
3. Class Method --> Needs minimum 1 arg,  decorator is needed

Q. What kind of method is __init__?
ans. It is an instance method because it doesn't have a decorator and needs minimum 1 arg(self).
'''

class Test:
    x=5
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):    #instance method
        print(self.a,self.b)
    @staticmethod       #decorator
    def f2():
        print('Hello')
    @classmethod
    def f3(cls):
        print(cls.x)

#objects
t1=Test(3,4)
t2=Test(5,6)
t1.show()
t2.show()
Test.f2()
Test.f3()   #class object
