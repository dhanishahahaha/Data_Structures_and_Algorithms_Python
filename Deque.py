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
