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
#print the first N natural numbers using recursion.
def printN(n):
    if n>=0:
        printN(n-1)
        print(n, end=" ")

printN(10)

#print the first N natural numbers in reverse using recursion.
def printNreverse(n):
    if n>=0:
        print(n, end=" ")
        printNreverse(n-1)

printNreverse(10)

#print the first N odd natural numbers using recursion.
def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1, end=" ")

printNodd(10)

#print the first N even natural numbers using recursion.
def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n, end=" ")

printNeven(10)

#print the first N natural numbers in reverse using recursion.
def printOddReverese(n):
    if n>0:
        print(2*n-1, end=" ")
        printOddReverese(n-1)

printOddReverese(10)

#print the first N even natural numbers in reverse using recursion.
def printEvenReverese(n):
    if n>0:
        print(2*n, end=" ")
        printEvenReverese(n-1)

printEvenReverese(10)

#print the sum of first N natural numbers using recursion.
def SumN(n):
    if n==1:
        return 1
    return n + SumN(n-1)

print("The sum is: ",SumN(10))

#print the sum of first N odd natural numbers using recursion.
def SumOddN(n):
    if n==1:
        return 1
    return 2*n-1 + SumOddN(n-1)

print("The sum of Odd numbers is :",SumOddN(10))

#print the sum of first N even natural numbers using recursion.
def SumEvenN(n):
    if n==1:
        return 2
    return 2*n + SumEvenN(n-1)

print("The sum of even numbers is :",SumEvenN(10))

#print the factorial of first N natural numbers using recursion.
def factorialN(n):
    if n==0:
        return 1
    return n * factorialN(n-1)

print("The factorial of numbers are: ", factorialN(10))

#print the sum of squares of N natural numbers using recursion.
def squares(n):
    if n==1:
        return 1
    return n**2 + squares(n-1)

print("the sum of square of numbers are: ",squares(5))