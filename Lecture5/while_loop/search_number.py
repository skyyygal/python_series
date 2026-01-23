# search for a number x in this tuple loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup =  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x=36
# input = int(input("Enter a number: "))

# while i<len(tup):
    # if(tup[i]==x):
        # print("Found at index", i)
    # else:
        # print("finding...")
    # i+=1

# to break the loop, we have other types such as break and continue.
# break: Used to terminate the loop when encountered. 
# continue: terminates the current iteration and continues execution of the loop with the next iteration.
  


while i<=5:
  if(i%2==0):
    i+=1
    continue
  print(i)
  i+=1