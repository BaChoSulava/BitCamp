import random

while True:
    level = input("Level: ")
    if level.isdigit() and int(level) > 0:
        user_guess = int(user_guess)        
        break

num = random.randint(1, int(level))

while True:
    user_guess = input("Guess: ")
    if user_guess.isdigit() and int(user_guess) > 0:
        num = int(num)
        break

if user_guess < num:
    print("Too small!")
elif user_guess > num:
    print("Too large!")
else:
    print("Just right!")