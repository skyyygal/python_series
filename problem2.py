# WAF that replaces the occurences of "Java" with "Python". 
# to replace. We must read the file, overwrite, then change. 


with open("practice.txt", "r") as f:
    data= f.read()

    new_data = data.replace("Java", "Python")
    print(new_data)

    # this does not replace the data in file. 

    # to do that, new we need to overwrite. 
with open("practice.txt", "w") as f:
    f.write(new_data)