def main():
    text = input("Input: ")
    ommit_vowels(text)

def ommit_vowels(text):
    omitted_text = ""
    vowels = ["A", "E", "I", "O", "U"]
    for letter in text:
        if letter.upper() in vowels:
            omitted_text += ""
        else:
            omitted_text += letter
    # print(omitted_text)
    return omitted_text


if __name__ == "__main__":
    main()