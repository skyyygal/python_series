# WAF to find in which line of the file does the does the learning word occur first. 
# print -1 if the word not found. 

word= "learning"
def check_for_word(word):
    with open("practice.txt", "r")as f:
        data = f.read()
        if(data.find(word)!=-1):
            print("Found")
        else:
            print("Not found")

def check_for_line():
    word = "learning"
    data = True
    line_no=1 
    with open("practice.txt", "r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1  
    
print(check_for_line())
    