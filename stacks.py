''' Stack
--> Stacks are Linear Data Structures.
--> Each stack is assumed to be inside a container with only its top side open, where only the top element of stack
    can be accessed at a time.
--> The working principle of stack is 'Last In First Out' (LIFO).
--> Operations on stack: A) Push B) Pop C) Peek D) is_empty E) size.

--> Implementation of Stack:- 
1. using List
2. by extending or inheriting a list class
3. 
  
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
--> Define a method insert() to restrict the insert function from the list class.
--> Implement a way to restrict the use of insert() method of list class from the stack object.
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