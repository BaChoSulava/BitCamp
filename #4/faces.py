
def convert(inp):
    return inp.replace(":)", "🙂").replace(":(", "🙁")
def main():
    inp = input("write text: ")
    print(convert(inp))


main()
