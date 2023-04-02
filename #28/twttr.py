def main():
    word = input("Input: ")
    shorten(word)

def shorten(word):
    omitted_text = ""
    vowels = ["A", "E", "I", "O", "U"]
    for letter in word:
        if letter.upper() in vowels:
            omitted_text += ""
        else:
            omitted_text += letter
    # print(omitted_text)
    return omitted_text


if __name__ == "__main__":
    main()

