def main():
    greeting = input("hay you greeting: ").lower().strip().split()
    first_word = greeting[0]
    print(value(first_word))


def value(first_word):
    if first_word == "hello":
        return "$0"
    elif first_word[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()