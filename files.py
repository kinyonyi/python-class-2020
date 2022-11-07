#reading and writing files 
"""
syntax is open(file, mode)
There are four different methods (modes) for opening a files

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

f = open("myfile.txt", "r")
print(f.read())
#to read a given number of characters 
print(f.read(10))
#writing to an existing files 
"a" #- Append - will append to the end of the file
"w" #- Write - will overwrite any existing content

f = open("filename.txt", "a")
f.write("Appended text to the specified file")
f.close()

#open and read the file after the appending:
f = open("filename.txt", "r")
print(f.read())

f = open("filename.txt", "w")
f.write("I have overwritten the contents of the file!")
f.close()

#open and read the file after the appending:
f = open("filename.txt", "r")
print(f.read())

#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist
#"w" - Write - will create a file if the specified file does not exist
f = open("myfile.txt", "x")
f = open("myfile.txt", "w")