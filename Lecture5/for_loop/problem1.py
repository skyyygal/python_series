list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in list:
    print(el)

# search the element
    tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
i = 0
for el in tup:
    if(el == x):
        print("Found at index: ", i )
    i+=1

