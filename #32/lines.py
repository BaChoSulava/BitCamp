import sys

#import file name
path = input("file's name or path: ")

print(sys.argv)

#checks for .py ending
if not path.endswith(".py") and len(sys.argv) != 1:
    sys.exit("File doesn't exist or too much arguments is written")

#counts lines
try:
    count = 0
    with open(path, "r") as file:
        for each_line in file:
            if not each_line.startswith("#") and not each_line.isspace():
                count += 1
        print("There is", count, "line code in the", path)
except FileNotFoundError:
    sys.exit("FileNotFoundError")