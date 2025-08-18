'''doubly linked list

DLL helps to propagate or move in both directions, every DLL node has a prev, item, next. 

--> make a node class to define a node 
--> make a DLL class with init method to create start refernce variable
--> make a function to check if the list is empty
--> make functions to insert nodes at the start, at last or between a particular node
--> make functions to delete nodes at the start, at last or between a particular node
--> make a function to search an item of the list
--> make a function to print the list
--> make a class and a function to iterate the list'''



class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty(): #if the list is not empty
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None: #if the list is not empty
            while temp.next!=None: #until none found in next of temp var
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:  #if None found after the start, insert n with start
            self.start=n
        else:
            temp.next=n   #otherwise insert n with the node that has None

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    

    def insert_after(self,temp,data):
        while temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None: #if there exists a node after temp var
                temp.next.prev=n
            temp.next=n 

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp=temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def delete_item(self,data):
        if self.start is None:
            pass 
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    

mylist=DLL()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
#use iterator to print list
for x in mylist:
    print(x,end=" ")
print()



