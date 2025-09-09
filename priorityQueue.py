'''
Priority Queue 

--> A collection of elements such that each element has been assigned a priority number.
--> The order of the elements are deleted and processed comes from the following rules:-
a) The element of the higher priority is processed before the element of the lower priority.
b) If two elements are of same priority then they are processed according to the order in which they were added 
   in the priority queue.

--> Elements can be inserted and deleted anywhere in the PQ.
   
--> Operation in the priority queue:-
a) push
b) pop
c) is_empty
d) size

--> Implementation of the priority queue:-
a) using the Linked List Concept
b) using Lists
c) using Heap

'''

#1. Implementation using List

#we are storing data and priority in the form of tuple in the list. 
#we have a list, that has indexes, at each index we have a tuple storing the data and the priority number.


class PriorityQueue:
    def __init__(self):
        self.items=[]  #initially empty

    def push(self,data,priority):
        index=0  #initial index of the list
        while index<len(self.items) and self.items[index][1]<=priority:   #1.check index and length of list, 2. check inside the list data[1] at a particular index should be less than or equal to priority number you wish to insert
            index+=1
        self.items.insert(index,(data,priority))

    def is_empty(self):
        return len(self.items)==0
    
    def pop(self):   #removes the highest priority element
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        else:
            return self.items.pop(0)[0]  #(0) --> index for the pop method, [0]--> data in the tuple of that index


#Usually, we do not pop any element in the Priority Queue but the one with the highest priority number, therefore, this method is only for practice.
    def pop_any(self,index=0): #to pop any priority element, 
        if self.is_empty():
            raise IndexError("Empty")
        else:
            if index<0 or index>=len(self.items):
                raise IndexError("Invalid Index")
            return self.items.pop(index)[0]  #in every index data,pri -- [0] is data

    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items


p=PriorityQueue()
p.push('D',4)
p.push('B',2)
p.push('C',3)
p.push('A',1)
p.push('F',6)
p.push('E',5)

print("Number of elements in the Priority Queue are: ",p.size())
print("priority queue: ",p.display())

p.pop()
print("Number of elements in the Priority Queue are: ",p.size())
print("priority queue: ",p.display())

p.pop_any(3)
print("Number of elements in the Priority Queue are: ",p.size())
print("priority queue: ",p.display())


while not p.is_empty():
    print(p.pop())


#2. Implementation of Priority Queue using Linked List Concept



    
