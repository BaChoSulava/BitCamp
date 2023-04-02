import sys

#import file name
path = input("file's name or path: ")

#checks for .py ending
if not path.endswith(".py"):
    sys.exit("FileNotFoundError")

#counts lines
count = 0
with open(path, "r") as file:
    for each_line in file:
        if not each_line.startswith("#") and not each_line.isspace():
            count += 1
    print("There is", count, "line code")
    