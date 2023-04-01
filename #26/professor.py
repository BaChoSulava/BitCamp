import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    
    while True:
        level = input("Level: ")
        if level in {"1", "2", "3"}:
            return int(level)
        print("Enter 1, 2 or 3")


def generate_integer(level):
    
    score = 0
    for i in range(10):
        X = random.randint(0, 10 * level)
        Y = random.randint(0, 10 * level)

        for _ in range(3):
            user_answer = input(f"{X} + {Y} = ")
            if not user_answer.isdigit() or (X + Y != int(user_answer)):
                print("EEE")
                continue
            elif X + Y == int(user_answer):
                score += 1
                break
        print(f"correct answer was: {X + Y}")
        continue
        
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
    
    