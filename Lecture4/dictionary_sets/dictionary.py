# Dictionary are used to store data values in lry:value pairs. 
# They are unordered, mutable(changeable) and don't allow duplicate keys. 

dict = {
    # keys cannot be dict or list
    "name": "Anita",
    "cgpa": "9.6",
    "marks":[98,97,95],
    "subjects":{"phy": 97, "chem": 98, "math":99}, #nested dictionalry
    "age":(4, 5, 6)
}
print(dict)
print(dict["marks"])
print(dict["age"][0])

dict["name"] ="Ano"
dict["Surname"] ="Pandey" 
print(dict)

null_dict = {}