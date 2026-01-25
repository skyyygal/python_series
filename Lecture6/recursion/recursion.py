# Recursion 
# When a function calls itself repeatedly
 
# PRINTS N TO 1 backwards

def show(n):
    if(n ==0): #Base case
        return
    print(n)
    show(n-1)

show(5)