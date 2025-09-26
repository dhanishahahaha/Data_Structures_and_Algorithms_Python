'''Heap
'''

'''
--> Make a class Heap to implement the Heap data structure with init method to create empty heap list.
--> In class Heap, define a method to create a heap from the given list of elements.
--> Define a method insert to insert a given element in the heap at the appropriate position.
'''

class EmptyHeapException(Exception):
    def __init__(self, message = "Heap is Empty!"):
        super().__init__(message)
        
class Heap:
    def __init__(self):
        self.heap = []
    
    def createHeap(self, items):
        for i in range(len(items)):
            self.insert(items[i], i)
    
    def insert(self,value, index):
        # temp = value
        self.heap.append(value)
        index = len(self.heap)-1
        parent = (index-1)//2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index-1)//2
    
    def top(self):
        if not self.heap:
            raise EmptyHeapException()
        else:
            return self.heap[0]
    
    
    def delete(self):
        if not self.heap:
            raise EmptyHeapException()
        last = self.heap.pop()
        index = 0
        if not self.heap:
            return last
        removed = self.heap[0]
        self.heap[index] = last
        
        while True:
            child1 = 2*index+1
            child2 = 2*index+2
            largest = index
        
            if child1 < len(self.heap) and self.heap[child1] > self.heap[largest]:
                largest = child1
            if child2 < len(self.heap) and self.heap[child2] > self.heap[largest]:
                largest = child2
            
            if index == largest:
                break
            
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            index = largest 
        return removed
           
    def heapSort(self, items):
        self.createHeap(items)
        sortedList = []
        
        while self.heap:
            sortedList.append(self.delete())
        
        print("Dscending Order:", sortedList)
        print("Ascending order", sortedList[::-1])
        
        
      
    def Print(self):
        print(self.heap) 
                    
h = Heap()
items = [40, 70, 10, 90, 60, 30, 50, 20, 80]
#h.createHeap(items)
h.Print()
h.delete()
h.Print()
print(f"Top Element is: {h.top()}")

list1=h.heapSort(items)
        
