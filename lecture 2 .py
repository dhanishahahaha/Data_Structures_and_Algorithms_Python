#Array and Lists

'''
Array is a collection of Homogenous data and a built in module, it needs to be imported.
It can support only limited type of data such as str,int,float and that's why Numpy is used more often.
Arrays have fixed size, dynamic arrays are growable.
Elements of the array can be indexed.
'''

from array import *
a1 = array('i',[11,12,14])
print(a1)

for x in a1:
    print(x)

for i in range(3):
    print(a1[i],end=' ')

i=0
while(i<len(a1)):
    print(a1[i])
    i+=1

#array methods
# 1. append
a1.append(20)
print(a1)

# 2. count
a1.count(100)

# 3. extend
a1.extend([23,24,25])
print(a1)

# 4. fromlist()


# 5. index()
a1.index(20)

# 6. insert()
a1.insert(5,54)
print(a1)

# 7. pop()
a1.pop()

# 8. remove()
a1.remove(12)
a1

# 9. reverse()
a1.reverse()
a1

# 10. tolist()
a1.tolist()
a1

'''
Lists is a class with heterogenous data, it is mutable and can be indexed.
Lists can grow because they use dynamic arrays.
'''

l1 = [23,34,56.98,'abcdef']
l2 = [] 

#methods in lists
#1. append()
l1.append('what')

#2. count()
l1.count(23)

#3. extend()
l1.extend([34.43,'eat'])

#4. index()
l1.index(34)

#5. insert()
l1.insert(3,41)

#6. pop()
l1.pop()

#7. remove()
l1.remove('eat')

#8. sort() -- will not be supported for heterogenous data types
l1.sort() 

#9. reverse()
l1.reverse()
l1

#10. clear()
l1.clear()
l1