# Search if the word "learning exists in the file or not"

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    # find= data.find("learning")
   
    if(data.find("learnings")!=-1):
        print("It exists")
    else:
        print("word does not exist")