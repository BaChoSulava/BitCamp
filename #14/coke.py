def main():
    coin = int(input("insert Coin: "))
    calculations(coin)

def calculations(coin):
    coin_range = [25, 10, 5]
    amount_due = 50

    while True:
        if coin not in coin_range:
            print (f"Amound Due: {amount_due}")
        amount_due -= coin
        if amount_due > 0 :
            
            print (f"Amound Due: {amount_due}")                  
            coin = int(input("insert Coin: ")) 
        else:
            print(f"Change Owed: {-1 * amount_due}")
            break
                

if __name__ == "__main__":
    main()