'''Recursion

--> Recursion means a function calling itself. 
--> Base Case: To stop calling the function anymore.
--> Recursive Case: To keep calling the function to solve the original problem.

Each time the recursive function calls itself for a little simpler version of the original problem.

eg: 
def f1(n):
    if n==1:  #base case
        return 1
    return n+f(n-1) #recursive case
    
'''

def printN(n):
    if n>=0:
        printN(n-1)
        print(n, end=" ")

printN(10)

def printNreverse(n):
    if n>=0:
        print(n, end=" ")
        printNreverse(n-1)

printNreverse(10)

def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1, end=" ")

printNodd(10)

def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n, end=" ")

printNeven(10)

def printOddReverese(n):
    if n>0:
        print(2*n-1, end=" ")
        printOddReverese(n-1)

printOddReverese(10)

def printEvenReverese(n):
    if n>0:
        print(2*n, end=" ")
        printEvenReverese(n-1)

printEvenReverese(10)