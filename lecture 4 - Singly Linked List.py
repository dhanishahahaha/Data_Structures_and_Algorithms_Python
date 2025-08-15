'''
define a class None to describe a node of a Singly Linked List
define a class SLL to implement Singly Linked List with init method to create and initialize start reference var.
define functions to insert items at the start, end and in the middle of a list
define functions to delete items at the start, end and in the middle of a list
define a function to print the list
define a function to search the elements of the list
define a class and function to make the SLL class iterable
'''

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
            return self.start == None
    
    def insert_at_start(self,data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty(): #means the list has nodes
            temp = self.start #making a temp var to traverse until reached the last node
            while temp.next is not None:
                temp = temp.next
            temp.next = n #to add the new node
        else:
            self.start = n #if the list is empty, simply attach the new node
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next=n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end= " ")
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            temp = self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                    
    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator: #to make the SLL class Iterable
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data



#driver code
mylist = SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(20)
mylist.print_list()

        