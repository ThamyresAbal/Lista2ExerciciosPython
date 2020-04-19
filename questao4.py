import os

dirlist = os.listdir(".")
for i in dirlist:
    filename = os.path.abspath(i)
    print(filename)