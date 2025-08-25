''' Stack
--> Stacks are Linear Data Structures.
--> Each stack is assumed to be inside a container with only its top side open, where only the top element of stack
    can be accessed at a time.
--> The working principle of stack is 'Last In First Out' (LIFO).
--> Operations on stack: A) Push B) Pop C) Peek D) is_empty E) size.

--> Implementation of Stack:- (5 different methods)
1. using List
2. by extending or inheriting a list class
3. using a Linked List
4. using already existing Singly Linked List code
5. by inheriting the SLL class in the Stack class
  
'''

# 1.Implementation of stack using list:-
'''
--> Define a class Stack to implement stack data structure using List. Define init method to create an 
    empty list object as instance object member of stack class.
--> Define a method is_empty() to check if the stack is empty or not.
--> Define a method push() to add an item to the top of the stack.
--> Define a method pop() to remove an item from the top of the stack.
--> Define a method peek() to return the top item of the stack without removing it.
--> Define a method size() to return the number of items in the stack.
--> Define a method display() to view elements of the entire stack from top to bottom.
'''

class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty(): #list not empty and has elements
            return self.items.pop()
        else: #for empty list
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty(): 
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.items)
    def display(self):
        return self.items[::-1]
    
myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
print("Items of the List are: ",myStack.display())
print("Top element is:",myStack.peek())
myStack.pop()
print("Top element is:",myStack.peek())
myStack.size()
print("Items of the List are: ",myStack.display())


# 2. Implementation of Stack by extending or inheriting a list class

'''
--> Define a class Stack inheriting a list class.
--> Define a method is_empty() to check if the stack is empty or not.
--> Define a method push() to add an item to the top of the stack.
--> Define a method pop() to remove an item from the top of the stack.
--> Define a method peek() to return the top item of the stack without removing it.
--> Define a method size() to return the number of items in the stack.
--> Implement a way to restrict the use of insert() method of list class from the stack object.
--> Define a method display() to show all the elements of the stack.
'''


class Stack(list):     #the child class can access the init of the parent class, so its not required here again
    def is_empty(self):
        return len(self)==0  #here self is a stack object but self can access both class
    def push(self,data):
        self.append(data)   #directly use the append function of the list class
    def pop(self):
        if not self.is_empty():
            return super().pop()  #simply using .pop() might override the pop func of the parent class, so we must use super() to show that it is a func from the parent class
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)
    def insert(self,index,data):   #we dont want to insert element randomly in stack, so we must restrict it
        raise AttributeError("No attribute 'insert' in Stack")
    def display(self):
        return self[::-1]

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("element removed: ",s1.pop())
print("top element of the stack is: ",s1.peek())
s1.size()
s1.push(50)
print("top element of the stack is: ",s1.peek())
#s1.insert(2,60)  throws attribute error
s1.display()


# 3. Implementation of stack using a Singly Linked list

''' The aim is to make a SLL which behaves as a stack using the concept of FILO, insertion, deletion and 
accessing at any one end of the list is possible.

--> make a SLL class to use the concept of stack, make a start var to initialize and item_count to keep a track
    of elements.
--> Define a method is_empty() to check if the stack is empty or not.
--> Define a method push() to add an item to the top of the stack.
--> Define a method pop() to remove an item from the top of the stack.
--> Define a method peek() to return the top item of the stack without removing it.
--> Define a method size() to return the number of items in the stack.
'''

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data):  #insertion only at the start or top
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
    def pop(self):
        if not self.is_empty(): #deletion only at the start or top of the list
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
    def peek(self):   #show only the start or top item of the stack
        if not self.is_empty():
            return self.start.item 
        else:
            raise self.is_empty()
    def size(self):
        return self.item_count
    def display(self):  #to display all the items of the stack
        temp=self.start
        if not self.is_empty():
            while temp is not None:
                print(temp.item, end=" ")
                temp=temp.next
            print()
        else:
            raise IndexError("Stack is Empty")
    
    
sll_as_stack=Stack()
sll_as_stack.push(40)
sll_as_stack.push(50)
sll_as_stack.push(60)
print("elements on the top: ",sll_as_stack.peek())
print("total elements in the stack are: ",sll_as_stack.size())
sll_as_stack.display()
sll_as_stack.pop()
print("elements on the top: ",sll_as_stack.peek())
print("total elements in the stack are: ",sll_as_stack.size())
sll_as_stack.display()

# 4. Implementation of Stack using Singly Linked List class 

'''
The aim is to make a Stack class which uses the previously made SLL class and implement its function on stack.
--> Import module containing SLL code 
--> Define a Stack class to implement the data structure Stack, define __init__ method to create SLL object.
--> Define a method is_empty() to check if the stack is empty or not.
--> Define a method push() to add an item to the top of the stack.
--> Define a method pop() to remove an item from the top of the stack.
--> Define a method peek() to return the top item of the stack without removing it.
--> Define a method size() to return the number of items in the stack.
--> Define a method display() to view all the elements of the stack.

'''

from SinglyLinkedList import *

class Stack:
    def __init__(self):
        self.mylist=SLL()  #sll object
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_empty()  #using already make is_empty func from the SLL class
    def push(self,data):
        self.mylist.insert_at_start(data)  #insertion and deletion only at first/top
        self.item_count+=1
    def pop(self):
        self.mylist.delete_first()
        self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item  #the reference of top node is in item of start in the SLL
    def size(self):
        return self.item_count
    def display(self):
        if not self.is_empty():
            self.mylist.print_list()
        else:
            raise IndexError("Stack is empty")
    
stacklist=Stack()
stacklist.push(90)
stacklist.push(80)
stacklist.push(70)
print("elements of the stack are: ")
stacklist.display()
print("element at the top: ",stacklist.peek())
stacklist.pop()
print("elements of the stack are: ")
stacklist.display()


# 5. Implementation of Stack by inheriting the class SLL

'''
Aim is to make a Stack class by inheriting the already existing SLL class

--> Import module containing SLL code 
--> Define a Stack class to implement the data structure Stack, inheriting the SLL class.
--> Define a method is_empty() to check if the stack is empty or not.
--> Define a method push() to add an item to the top of the stack.
--> Define a method pop() to remove an item from the top of the stack.
--> Define a method peek() to return the top item of the stack without removing it.
--> Define a method size() to return the number of items in the stack.
--> Define a method display() to view all the elements of the stack.
'''

from SinglyLinkedList import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack Underflow")
    def size(self):
        return self.item_count
    
    def display(self):
        if not self.is_empty():
            self.print_list()
        else:
            raise IndexError("Stack Underflow")
    
sll_in_stack=Stack()
sll_in_stack.push(101)
sll_in_stack.push(102)
sll_in_stack.push(103)
print("first element is: ",sll_in_stack.peek())
print("Elements of the stack are: ")
sll_in_stack.display()
sll_in_stack.size()
sll_in_stack.pop()
print("first element is: ",sll_in_stack.peek())
sll_in_stack.size()
print("Elements of the stack are: ")
sll_in_stack.display()
