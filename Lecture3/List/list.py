student = ["anita", 67, "Delhi, 56.7"]
print(student)
print(type(student[0]))

# list donot have specific type in python, it can hold any data type. 
#  strings -> immutable. list-> mutable in python.
# for eg: 
# str = "anita"
# print(str[0])
# str[0] = "o"  #throws error. Not possible in string coz it's immutable. 

student = ["anita", 67, "Delhi, 56.7"]
student[0] = "anita pandey"
print(student)

# List slicing - is similar to string slicing 
print(student[1:2]) #sublist 

marks = [87, 64, 33, 95, 76]
print(marks[:4])
print(marks[-4:-1])



# List Methods
list = [2,1,3]
print(list.append(4))

print(list.sort())
print(list.sort(reverse=True))

print(list.reverse())
print(list.insert(3, 4)) 
list.remove(1) #removes 1 in the list 
list.pop(1) #removes element in index 1
# this all the print statement prints none. no point of printing list with methods. 

print(list)
list2 = ["Banana", "Apple", "Avocado"]
list2.sort()
print(list2)
