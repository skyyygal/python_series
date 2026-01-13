# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list = [1,2,3,2,1]

list2 = list.copy()

list2.reverse()

if(list == list2):
    print("palindrome")

else: 
    print("Not a palindrome")