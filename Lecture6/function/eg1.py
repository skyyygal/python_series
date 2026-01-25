a=5
b=10
sum = a+b
print(sum)

# In this scenario if we want to add other values, 
# this lets us repeat the same lines of code. 
# function resolves recursion. It is adviced when the same method is repeated twice or more. Convert it to fn. 
# redundant is something that's repeated. 

def sum1(a, b):
    c = a+b
    print(c)
    return c

sum1(5,5)

# default parameters, fn with return val and fn without return val. 