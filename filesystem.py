import os
#getting the cureent working directory 
current = os.getcwd()
print(current)
changed = os.path.join(current, "movies")
print(changed)
#creation of directory
try:
    os.makedirs("images")
    print("images have been created successfuly")
except FileExistsError as e:
    print(str(e))
    #deleting the folder 
    #os.removedirs("images")
os.chdir("images")
print(os.getcwd())
os.chdir("..")
#listing the files in the folder
directory_content = os.listdir()
print(directory_content)
#checking whther a given path is a folder or a file 
pa = os.path.join(os.getcwd(),"classes.py")
print(os.path.isfile(pa))
#check whether is a directory
print(os.path.isdir(pa))
#get the file size of a given file
print(os.path.getsize(pa))#returns ,the size in bytes
#os.chdir("images")
#os.unlink("davis.txt")
#os.remove("davis.txt")
print(os.getcwd())
total_size = 0
files = os.listdir(os.getcwd())
for file in files:
    total_size += os.path.getsize(file)
print(total_size)
#os.path.join(".","davis.txt")
os.chdir("images")
open("dave.css","x")