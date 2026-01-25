# WAF to print the elements of a list in a single line.
# hover over the print() function. 
# You will understand it's additional features, 
# You have a seperator, end. Which will allow you to print element in a line. 

print()
heroes = ["Thor", "ironman", "spiderman", "superman", "batman"]
cities = ["Chennai", "Bengaluru", "Mumbai", "Pune", "Hyderabad", "Delhi"]


def print_el(list):
    for i in list:
    #  print(i, end="\n") #prints element in a next line. 
     print(i, end=" ")

print_el(heroes)

