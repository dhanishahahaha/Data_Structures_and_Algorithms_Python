'''
Python: Dynamically typed language
DSA - Data Structures and Algorithms

Classification : Linear and Non Linear Data Structures
Linear --> Array, dynamic array, linked lists, stack, queue, deque, etc
Non- Linear --> BST, AVL, B-Tree, B+Tree, graph, etc

Algorithm: A step by step linguistic representation of logic to solve a given problem.
'''

#Array and Lists

'''
Array is a collection of Homogenous data and a built in module, it needs to be imported.
It can support only limited type of data such as str,int,float and that's why Numpy is used more often.
Arrays have fixed size, dynamic arrays are growable.
Elements of the array can be indexed.

Q. What is the difference between Array and a dynamic array?
ans. Array is of a fixed size, dynamic array is resizable.
'''

from array import *
a1 = array('i',[11,12,14])
print(a1)

for x in a1:
    print(x)

for i in range(3):
    print(a1[i],end=' ')

i=0
while(i<len(a1)):
    print(a1[i])
    i+=1

#array methods
# 1. append
a1.append(20)
print(a1)

# 2. count
a1.count(100)

# 3. extend
a1.extend([23,24,25])
print(a1)

# 4. fromlist()
temp_list = [99, 100, 101]
a1.fromlist(temp_list)
print("After fromlist:", a1)


# 5. index()
a1.index(20)

# 6. insert()
a1.insert(5,54)
print(a1)

# 7. pop()
a1.pop()

# 8. remove()
a1.remove(12)
a1

# 9. reverse()
a1.reverse()
a1

# 10. tolist()
a1.tolist()
a1

'''
Lists is a class with heterogenous data, it is mutable and can be indexed.
Lists can grow because they use and are up of dynamic arrays.
'''

l1 = [23,34,56.98,'abcdef']
l2 = [] 

#methods in lists
#1. append()
l1.append('what')

#2. count()
l1.count(23)

#3. extend()
l1.extend([34.43,'eat'])

#4. index()
l1.index(34)

#5. insert()
l1.insert(3,41)

#6. pop()
l1.pop()

#7. remove()
l1.remove('eat')

#8. sort() -- will not be supported for heterogenous data types
l1.sort() 

#9. reverse()
l1.reverse()
l1

#10. clear()
l1.clear()
l1

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
