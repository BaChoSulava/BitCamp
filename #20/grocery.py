def main():
    create_grocery_list(item = "")

def create_grocery_list(item = ""):
    grocery_items = []
    n = 1
    while True:
        try:
            item = input("Item: ")
            if not item:
                continue
            if item.isdigit():
                break
        except EOFError:
            break
        item = item.upper()
        grocery_items.append(item)
    for i in sorted(grocery_items):
        print(f"{n}. {i}")
        n += 1
    

if __name__ == "__main__":
    main()
    