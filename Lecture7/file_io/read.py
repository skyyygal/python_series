f = open("demo.txt", "r")
# data = f.read()
data = f.readline()
print(data)
print(type(data))
f.close()

# data = f.read() #reads entire file

# data = f.readline() #reads one line at a time