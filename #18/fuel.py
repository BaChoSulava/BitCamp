def main():
    fraction = input("Fraction: ")
    calc_percentage(fraction)

def calc_percentage(fraction):

    while True:
        try:
            fraction = input("Fraction: ")
            fraction_split = fraction.split("/")
            percentage = int(fraction_split[0]) * 100 / int(fraction_split[1])
            rounded_percentage = round(percentage)
            print(f"{rounded_percentage}%")

            if rounded_percentage <= 1:
                print("E")
                return "E"
            if rounded_percentage > 100:
                print("X is greater then Y, try again")
                continue
            if  rounded_percentage >= 99:
                print("F")
                return "F"
            
            return f"{rounded_percentage}%"  
        
        except ValueError:
            print("Wrong value")
        except ZeroDivisionError:
            print("Can't devide bty 0")

        
            
    
        
        
    

if __name__ == "__main__":
    main()