def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    #options for validation
    a = plate[0:2].isalpha()
    b = 2 <= len(plate) <= 6
    
    c = True
    for letter in plate:
        if letter.isdigit():
            # if plate.index(letter) == 0:
                if not plate[plate.index(letter):].isdigit():
                    c = False

    bad_symbol = ",.- _?!:"
    d = True
    for letter in plate:
        if letter in bad_symbol:
            d = False
            
    print(a,b, c, d)
    
    #check if every option is valid
    if a and b and c and d:
        return True
    else:
        return False

if __name__ == "__main__":
    main()