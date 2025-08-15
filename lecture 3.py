'''Classes and Objects
there are two types of objects in Python: instance and class
'''
class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

t1 = test(3,4)
t2 = test(7,8)
print(t1.a , t1.b)
print(t2.a , t2.b)