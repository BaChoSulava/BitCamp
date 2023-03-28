def main():
    order = input("Item: ")
    users_order(order)

def users_order(order):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    try: 
        while True:
            total += menu[order]
            total_formatted = f"{total:.2f}"
            print(f"Total: ${total_formatted}")
            order = input("Item: ")
    except EOFError:
        return f"Total: ${total_formatted}"

if __name__ == "__main__":
        main()
