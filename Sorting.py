'''Sorting'''

'''
--> Write a python code to implement bubble sorting.
--> Write a python code to implement modified bubble sort.
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
    