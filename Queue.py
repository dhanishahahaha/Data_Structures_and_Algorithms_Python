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


# 1. Implementation of Queue using Singly Linked List concept
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

class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None  #deletion
        self.rare=None   #insertion
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.rare=n
            self.front=n
        else:
            self.rare.next=n
            self.rare=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        elif self.rare==self.front:
            self.rare=None
            self.front=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else:
            return self.front.item
    def get_rare(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else:
            return self.rare.item
    def size(self):
        return self.item_count
    def display(self):
        temp=self.front
        if not self.is_empty():
            while temp is not None:
                print(temp.item, end=" ")
                temp=temp.next
            print()
        else:
            raise IndexError("Queue Underflow")
        
q2=Queue()
q2.enqueue(100)
q2.enqueue(101)
q2.enqueue(102)
q2.enqueue(103)
q2.enqueue(104)
print("the size of the queue is ",q2.size())
q2.display()
print("The rare element is",q2.get_rare())
print("The front element is",q2.get_front())
q2.dequeue()
print("the size of the queue is ",q2.size())
q2.display()
print("The rare element is",q2.get_rare())
print("The front element is",q2.get_front())