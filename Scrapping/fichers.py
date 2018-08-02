import os

os.chdir("C:/dir1/dir2")
os.chdir("C:\\dir1\\dir2")
os.chdir(r"C:\dir1\dir2")

ficher = open("ficher.txt", "r")  # only to read; a pour append
data = ficher.read()
ficher.close()  # don't forget to close

ficher = open("ficher.txt", "w")  # to write
ficher.write("only a string")
ficher.close()  # don't forget to close

with open("ficher.txt", "r") as ficher:  # to close it automatically
    pass

#  __enter__ __exit__


