'''Sorting'''

'''
--> Write a python code to implement bubble sorting.
--> Write a python code to implement modified bubble sort.
--> Write a python code to implement the selection sort.
--> Write a python code to implement the insertion sort.
'''

#Implementation of Bubble sort
def bubble_sort(data_list):
    for r in range(1,len(data_list)):  #no of rounds
        for i in range(len(data_list) - r): #n-1 comparisions for every round
            if data_list[i] > data_list[i+1]:
                data_list[i] , data_list[i+1] = data_list[i+1] , data_list[i]

l=[34,67,12,89,25,50]
bubble_sort(l)
print(l)


#implementation of Modified bubble sort
def modified_bubble_sort(data_list):
    flag=False  #before every round flag=False, if swapping happens flag=True
    for r in range(1,len(data_list)):  #no of rounds
        flag=False
        for i in range(len(data_list) - r):
            if data_list[i]>data_list[i+1]:
                data_list[i] , data_list[i+1] = data_list[i+1],data_list[i] #swapping
                flag=True 
        if not flag:  #if no swapping then flag=False, and break
            break

l=[34,67,12,89,25,50]
modified_bubble_sort(l)
print(l)
    

#Implementation of the selection sort

def selection_sort(list1):
    n = len(list1)
    for i in range(n):  #loop on all elements of list1
        min_index=i #index of the smallest element
        for j in range(i+1,n): #comparision of all elements with i, to find if there exists a smaller element than i
            if list1[j]<list1[min_index]: #if another index j is smaller than i
                min_index=j #then update min_index with j
        list1[i], list1[min_index] = list1[min_index], list1[i] #swap i with the smallest index found 

l=[22,67,48,13,89,54,21]
selection_sort(l)
print(l)
