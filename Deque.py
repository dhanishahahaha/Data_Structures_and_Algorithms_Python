'''Deque

--> The principle of Queue is First In First out.
--> Queues have restriction on Insertion and Deletion both, only insertion and deletion can be done from one 
end each.

--> Variations of Queue:-
    a) Insertion Restricted - Only insert from one end but deletion from both ends.
    b) Deletion Restricted - Only delete from one end but insertion from both ends.
    c) Deque - NO RESTRICTIONS, insertion from both ends, deletion from both ends.
--> Deque is "Double Ended queue"
--> It is a Linear Data Structure.

--> Operations on Deque:-
    a) Insert_front
    b) Insert_rare
    c) delete_front
    d) delete_rare
    e) get_front
    f) get_rare
    g) is_empty
    h) size
    i) display

--> Implementation of Deque:-
    a) using List class
    b) by Inheriting list class
    c) using DLL class
    d) by inheriting DLL class
    e) using the concept of linked list class

Q) Why use DLL here and not SLL?
Ans) To be able to traverse in both directions due to insertion and deletion on both ends.
'''

#1. Implementation of Deque using List class

'''
--> make a Deque class to use the concept of deque, define an init method and make an empty list.
--> Define a method is_empty() to check if the deque is empty or not.
--> Define a method insert_front() to add an item to the front of the deque.
--> Define a method insert_rare() to add an item to the rare of the deque.
--> Define a method delete_front() to delete an item at the front of the deque.
--> Define a method delete_rare() to delete an item at the rare of the deque.
--> Define a method get_front() to view an item at the front of the deque.
--> Define a method get_rare() view an item at the rare of the deque.
--> Define a method size() to return the number of items in the deque.
--> Define a method display() to view all the elements of the deque.
'''

class Deque:
    def __init__(self):
        self.items=[]
        self.item_count=0
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rare(self,data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.items.pop(0)
    def delete_rare(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.items.pop()
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.items[0]
    def get_rare(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
        

q1=Deque()
q1.insert_front(10)
q1.insert_front(20)
q1.insert_front(25)
q1.insert_rare(30)
q1.insert_rare(40)
q1.insert_rare(50)
print("Number of elements are: ",q1.size())
q1.display()
print("Front element is ",q1.get_front())
print("Rare element is ",q1.get_rare())    
q1.delete_front()
q1.delete_rare()
print("Number of elements are: ",q1.size())
q1.display()
print("Front element is ",q1.get_front())
print("Rare element is ",q1.get_rare())    



#2. Implementation of Deque using Doubly Linked List 

'''
--> make a Node class to initialize prev, item, next
--> make a Deque class to use the concept of deque, define an init method and make an empty list.
--> Define a method is_empty() to check if the deque is empty or not.
--> Define a method insert_front() to add an item to the front of the deque.
--> Define a method insert_rare() to add an item to the rare of the deque.
--> Define a method delete_front() to delete an item at the front of the deque.
--> Define a method delete_rare() to delete an item at the rare of the deque.
--> Define a method get_front() to view an item at the front of the deque.
--> Define a method get_rare() view an item at the rare of the deque.
--> Define a method size() to return the number of items in the deque.
--> Define a method display() to view all the elements of the deque.
'''

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.item_count==0

    def insert_front(self,data):
        n=Node(None,data,self.front) #prev,item,next
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.front.prev=n
            self.front=n
        self.item_count+=1
    def insert_rear(self,data):
        n=Node(self.rear,data,None) #prev,item,next
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        self.item_count+=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque Underflow")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque Underflow")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque Underflow")
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque Underflow")
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count
    
    def display(self):
        temp=self.front
        if self.is_empty():
            raise IndexError("Deque Underflow")
        else:
            while temp is not None:
                print(temp.item, end= " ")
                temp=temp.next
            print() #new line clean output

d2=Deque()
d2.insert_front(1)
d2.insert_front(2)
d2.insert_front(3)
d2.insert_front(4)
d2.insert_front(5)
d2.insert_rear(6)
d2.insert_rear(7)
d2.insert_rear(8)
d2.insert_rear(9)
d2.insert_rear(10)
print("The front element is :",d2.get_front())
print("The rear element is :",d2.get_rear())
print("Number of items in the deque: ",d2.item_count)
print("Elements of the deque: ")
d2.display()
d2.delete_front()
d2.delete_rear()
print("The front element is :",d2.get_front())
print("The rear element is :",d2.get_rear())
print("Number of items in the deque: ",d2.item_count)
print("Elements of the deque: ")
d2.display()