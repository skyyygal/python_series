# WAP to find the greatest of 3 numbers entered by the user


a=input("Enter the first number: ")
b=input("Enter the second number: ")
c=input("Enter the third number: ")

if(a>b and a>c):
    print(a, "is greater")
elif(b>a and b>c):
    print(b, "is greater")
else: 
    print(c, "is greater")