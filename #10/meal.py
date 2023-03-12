def main():
    time = input("input time: ")
    time = convert(time)

    if 18 <= time <=19:
        print("It's dinner time")
    elif 12 <= time <= 13:
        print("It's lunch time")
    elif 7 <= time <= 8:
        print("It's breakfast time")
        
   
def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes)/60
    return time

if __name__ == "__main__":
    main()
