import os 
# import os as o
# from os import *
# from os import getcwd

file = input("Enter your file : ")
folder = input("Enter your folder : ")

# PRESENT WORKING DIRECTORY
print(os.getcwd())

# LIST OF FILE
print(os.listdir())

# DELETE FILE 
print(os.remove(file))

# CREATE FOLDER
print(os.mkdir(folder))

# DELETE FOLDER 
print(os.rmdir(folder))

# OS CONTAIN
print(dir(os))
