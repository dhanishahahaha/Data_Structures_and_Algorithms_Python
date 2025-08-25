''' Stack
--> Stacks are Linear Data Structures.
--> Each stack is assumed to be inside a container with only its top side open, where only the top element of stack
    can be accessed at a time.
--> The working principle of stack is 'Last In First Out' (LIFO).
--> Operations on stack: A) Push B) Pop C) Peek D) is_empty E) size.

--> Implementation of Stack:- 
1. using List
2. by extending a list class
3. 
  
'''

#Implementation of stack using list:-
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