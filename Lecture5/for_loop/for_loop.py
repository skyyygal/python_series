# Loops are used for sequential traversal. For traversing list, string, tuple etc.

"for loop"
# for el in list:
    # some work

"for loop with else"
# for el in list:
#  "some work"
#else: 
#  "work when loop ends"

list = [1,2,3]
for el in list:
    print(el)

for el in list:
    print(el, "one")
else: 
    print("loop ends")