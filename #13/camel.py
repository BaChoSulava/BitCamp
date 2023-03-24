def main():
    name = input("name of variable please: ")
    convert_to_snake(name)
    

def convert_to_snake(name):
    name_snake = ""
    for letter in name:
        if letter.isupper():
           name_snake += "_" + letter.lower()
        else:
            name_snake += letter.lower()
    print(name_snake)
    return name_snake


if __name__ == "__main__":
    main()

