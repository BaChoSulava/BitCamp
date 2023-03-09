
def convert(inp):
    match inp:
        case ":)":
            return "🙂"
        case ":(":
            return "🙁"
        case _:
            return inp
def main():
    inp = input("write text: ")
    print(convert(inp))


main()
