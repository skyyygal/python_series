# WAP to check if a number is a multiple of 7 or not. 
# solution: to check the percular number when divided by 7 returns 0 as a reminder. 

print("Check the number is divisible by 7")
a = int(input("Enter a number: "))

if(a%7==0):
    print(a, "is multiple of 7")

else:
    print(a,"is not multiple of 7")