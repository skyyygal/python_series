# 0! and 1! = 1

# 2! = 1*2
# 3! = 1*2*3 => 2!*3
# 4! = 1*2*3 => 3!*4
# 5! = 1*2*3*4 => 4!*5

# n! = (n-1)*n
# fact(n)= fact(n-1)*n
# fact(n-1)= fact(n-2)*(n-1)



def fact(n):
    if(n==1 or n==0): #this is base case, stopping condition.
        return 1

    return fact(n-1) * n


print(fact(6))