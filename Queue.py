''' Queue

--> looks like a cylinder or pipe with flowing water.
--> A linear data structure.
--> Works on the principle of First in First Out (FIFO)
--> Rare is the insertion element in a queue and Front is the deletion element in a queue

--> Operations on Queue:-
    a)enqueue - Insertion (rare)
    b)dequeue - Deletion (front)
    c)is_empty
    d)get_front - see front value
    e)get_rare - see rare value
    f)size

--> Implementation of Queue:-
    a) using Lists
    b) by extending list class
    c) using SLL class
    d) by extending SLL class
    e) using Linked List concept
'''

# 1. Implementation of Queue using List
'''
--> Define a class Queue to implement Queue data structure. Define init method to create an empty list object 
    as instance object member of queue.
--> Define a method is_empty() to check if the queue is empty or not.
--> Define a method enqueue() to add an item to the queue.
--> Define a method dequeue() to remove an item from queue.
--> Define a method get_front() to return the top item of the queue without removing it.
--> Define a method get_rare() to return the last item of the queue without removing it.
--> Define a method size() to return the number of items in the queue.
--> Define a method display() to view elements of the entire stack from top to bottom.
'''

class Queue:
    def __init__(self):
        self.list=[]
    
    def is_empty(self):
        return len(self.list)==0
    
    def enqueue(self,data):
        self.list.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Queue Underflow")
        
    def get_rare(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Queue Underflow")
        
    def size(self):
        return len(self.list)
    
    def display(self):
        if not self.is_empty():
            return self.list
        else:
            raise IndexError("Queue Underflow") 
        
q1 = Queue()
try:                          #exception handling to get only the errors we want without any exceptions
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
    

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print("Number of elements in queue are: ",q1.size())
print(q1.get_front())
print(q1.get_rare())
print(q1.display())
q1.dequeue()
print("Number of elements in queue are: ",q1.size())
print(q1.get_front())
print(q1.get_rare())
print(q1.display())