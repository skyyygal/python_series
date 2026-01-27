# File I/O in python. 
# python can be used to perform operations on a file. (read and write data)

# type of all files 
"1. Text Files : .txt, .docx, .log etc."
"Binary Files : .mp4, .mov, .png, .jpeg etc."

"Open, read and close File."
# We have to open a file before reading or writing. 

f = open("file_name", "mode")

"file_names: "
# same.txt
# demo.docx

"mode: "
# r: read mode 
# w: write mode


data = f.read()
f.close()

'types of modes'
"""
'r' - open for reading(default)
'w' - open for writing, truncating the file first
'x' - create a new file and open it for writing
'a' - open for writing, appending to the end of the file, it it exists.
'b' - binary mode
't' - text mode(default)
'+' - open a disk file for updating (reading and writing)
"""