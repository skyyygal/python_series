# WA recursive fn to print all elements in a list
# hint: use list and index as params. 

def print_el(list, idx):
    if(idx==len(list)):
        return 0
    print(list[idx])
    print_el(list, idx+1)

n = [1, 2, 2, 4, 6, 8]

print_el(n, 0)