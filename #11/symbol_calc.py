text = input("What is the input string? ") 
sum = len(text)

while sum == 0:
    text = input("you have to write something: ")
    sum = len(text)
print(f"'{text}' has {sum} characters.")