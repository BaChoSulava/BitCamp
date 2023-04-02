def main():
    fraction = input("Fraction: ")
    rounded_percentage = convert(fraction)
    print(gauge(rounded_percentage))

def convert(fraction):

    while True:
        try:
            fraction = input("Fraction: ")
            fraction_split = fraction.split("/")
            percentage = int(fraction_split[0]) * 100 / int(fraction_split[1])
            rounded_percentage = round(percentage)
            
            if rounded_percentage > 100:
                print("X is greater then Y, try again")

            return rounded_percentage
        
        except ValueError:
            print("Wrong value")
        except ZeroDivisionError:
            print("Can't devide bty 0")

def gauge(rounded_percentage):
    if rounded_percentage <= 1:
        return "E"
    if  rounded_percentage >= 99:
        return "F"
    
    return f"{rounded_percentage}%"  

if __name__ == "__main__":
    main()