# WAF to find the factorial of n. (n is the parameter)



def cal_fact(n):
    f=1 
    for i in range(1, n+1):
        f *= i   
    print(f)

cal_fact(5)
