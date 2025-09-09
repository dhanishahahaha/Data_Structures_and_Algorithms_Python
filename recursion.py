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