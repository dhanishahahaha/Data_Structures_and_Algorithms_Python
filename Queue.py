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
    b) by inheriting a list class
    c) using SLL class
    d) by inheriting a SLL class
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


#2. Implementation of Queue by Inheriting a List
'''
--> Define a class Queue inheriting a list class.Define init method to create an empty list object 
    as instance object member of queue.
--> Define a method is_empty() to check if the queue is empty or not.
--> Define a method enqueue() to add an item to the queue.
--> Define a method dequeue() to remove an item from queue.
--> Define a method get_front() to return the top item of the queue without removing it.
--> Define a method get_rare() to return the last item of the queue without removing it.
--> Define a method size() to return the number of items in the queue.
--> Define a method display() to view elements of the entir

'''

class Queue(list):
    def is_empty(self):
        return len(self)==0 #because self is a part of class List which is inherited

    def enqueue(self,data):
        self.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Queue Underflow")
    
    def get_front(self):
        if not self.is_empty():
            return self[0]
        raise IndexError("Queue Underflow")
    
    def get_rare(self):
        if not self.is_empty():
            return self[-1]
        raise IndexError("Queue Underflow")
    
    def size(self):
        return len(self)
    
    def display(self):
        return self[::-1]
    
q3=Queue()
q3.enqueue(1)
q3.enqueue(2)
q3.enqueue(3)
q3.enqueue(4)
print("top element: ",q3.get_front())
print("last element: ",q3.get_rare())
print("elements of the queue are: ",q3.display())
print("size of the queue is: ",q3.size())
q3.dequeue()
print("top element: ",q3.get_front())
print("last element: ",q3.get_rare())
print("elements of the queue are: ",q3.display())
print("size of the queue is: ",q3.size())


#3. Implementation of queue by using a already made Singly Linked list

''' 
--> Use the SLL class to implement the concept of queue, use the SLL to initialize and item_count to keep a track
    of elements.
--> Define a method is_empty() to check if the queue is empty or not.
--> Define a method enqueue() to add an item to the queue.
--> Define a method dequeue() to remove an item from queue.
--> Define a method get_front() to return the top item of the queue without removing it.
--> Define a method get_rare() to return the last item of the queue without removing it.
--> Define a method size() to return the number of items in the queue.
--> Define a method display() to view elements of the entire stack from top to bottom.
'''

from SinglyLinkedList import * 

class Queue:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        else:
            delete= self.mylist.delete_first()
            self.item_count-=1
            return delete
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.item
        raise IndexError("Queue Underflow")

    def get_rare(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        temp = self.mylist.start
        while temp.next is not None:
            temp = temp.next
        return temp.item
        
        
    def size(self):
        return self.item_count


    def display(self):
        temp=self.mylist.start
        if not self.is_empty():
            while temp is not None:
                print(temp.item, end=" ")
                temp=temp.next
            print()
        
q4=Queue() # front element --- more elements --- rare element
q4.enqueue(50)
q4.enqueue(51)
q4.enqueue(52)
q4.enqueue(53)
q4.enqueue(54)
print("the size of the queue is ",q4.size())
q4.display()
print("The rare element is",q4.get_rare())
print("The front element is",q4.get_front())
q4.dequeue()
print("the size of the queue is ",q4.size())
q4.display()
print("The rare element is",q4.get_rare())
print("The front element is",q4.get_front())


#4. Implementation of queue by inheriting a SLL class

'''
Aim is to make a queue class by inheriting the already existing SLL class

--> Import module containing SLL code 
--> Define a Queue class to implement the data structure Queue, inheriting the SLL class.
--> Define a method is_empty() to check if the queue is empty or not.
--> Define a method enqueue() to add an item to the queue.
--> Define a method dequeue() to remove an item from queue.
--> Define a method get_front() to return the top item of the queue without removing it.
--> Define a method get_rare() to return the last item of the queue without removing it.
--> Define a method size() to return the number of items in the queue.
--> Define a method display() to view elements of the entire stack from top to bottom.
'''

from SinglyLinkedList import *

class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0

    def is_empty(self):
        return super().is_empty()
    
    def enqueue(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def dequeue(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Queue Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Queue Underflow")
        
    def get_rare(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        raise IndexError("Queue Underflow")
    
    
    def size(self):
        return self.item_count
    
    def display(self):
        if not self.is_empty():
            temp=self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp=temp.next
            print()
        else:    
            raise IndexError("Queue Underflow")
    
        
    

q5=Queue()
q5.enqueue(111)
q5.enqueue(222)
q5.enqueue(333)
q5.enqueue(444)
q5.enqueue(555)
print("the size of the queue is ",q5.size())
q5.display()
print("The rare element is",q5.get_rare())
print("The front element is",q5.get_front())
q5.dequeue()
print("the size of the queue is ",q5.size())
q5.display()
print("The rare element is",q5.get_rare())
print("The front element is",q5.get_front())
    
    

#5. Implementation of Queue using Singly Linked List concept
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