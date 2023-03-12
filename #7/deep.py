answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip() 
correct_answer = ["42", "forty-two", "forty two"]

if answer in correct_answer:
    print("Yes")
else:
    print("No")
