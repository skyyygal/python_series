with open("demo.txt", 'r') as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("new data")


    # while using with keyword you don't necessarily need to close the file. it closes on default