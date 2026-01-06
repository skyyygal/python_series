#String is a data type that stores a sequence of characters. 

"""
* concatenation 
"hello" + "world" -> "helloworld"

* length of str
 len(str)

"""

str1 = "this is a string."
str2 = 'Anita'
str3 = """this is a string"""
hello = 'Hello'
name = 'Anita'
str4 = "This is a string. We are creating it in python."
# next line - escape sequence characters. 
str4 = "This is a string. \nWe are creating it in python."
str4 = "This is a string. \tWe are creating it in python."
# print(str4)

# concatenation
print(hello+name)
final_str = hello + ' ' + name
print(final_str)

# length
# print(len(name))

print(len(final_str))

# Index - Positioning of the characters
""" 
str = 'A n i t a' 
       0 1 2 3 4 
  """

ch = str2[0]
str1 = "anita pandey"
# str1[4] = '@' manimulation cannot happen. It'll throw error
print(str1)
# print(ch)

# Slicing - returns the character of the given frm to end index.
# str[starting_idx : ending_idx]
# str[:ending_idx] = str[0:ending_idx]
# str[starting_idx:] = str[starting_idx:ending_idx]

str = "Anita Pandey"
ch = str [1:4]
ch = str[:4]
ch1 = str[0:]
ch1 = str[0:len(str)]

print(ch)
print(ch1)


# Case 2 - Slicing / Negative Index(special in python)
# A  P  P  L  E 
#-5 -4 -3 -2 -1

str = "Apple"
ch = str[-3:-1]
print(ch) #pl

# String function 
'''
str = "I am a coder."
str.endsWith("er") #returns true or false
str.capitalize() #capitalize 1st character. 
str.replace(old, new) #replace old with new char. 
str.find(word)
str.count("am") #count the occorance of substring in string. 
'''

str = "I am a coder."
print(str.endswith('er'))
print(str.capitalize())
print(str.replace("I am a coder", "I love coding"))
print(str) #note: the actual string is not replaced
print(str.find("code"))
print(str.count('a'))

