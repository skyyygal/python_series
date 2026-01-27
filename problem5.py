# From a file containing numbers seperated by comma, print the count of even numbers.

# extract the individual number.
# parsing or casting data to int as substring
# we have split method in py to get the individual number. 
def print_even_num():
    
    with open("num.txt", "r") as f:
        data = f.read()
        print(data)
    nums = data.split(",")
    # print(nums)
    count = 0

    for val in nums:
        # print(val)
        if(int(val) % 2==0):
          count+=1
    print(count)
    
    # without split
    # num = ""
    # for i in range(len(data)):
        # if(data[i]==","):
            # print(num)
            # num = ""
        # else:
            # num += data[i]
    




  

print_even_num()