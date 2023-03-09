import time

def calc_BMI():
    print()
    print("Ok, let's calculate your BMI!!!")
    time.sleep(1)
    unit = input("Do you prefere Metric or US units? ").lower()
    time.sleep(1)
    match unit:
        case "metric":
            weight = float(input("What is your weight in kg? : "))
            time.sleep(0.5)
            height = float(input("And height in cm : ")) / 100
        case "us":
            weight = float(input("What is your weight in pounds? : ")) * 2.20462
            time.sleep(0.5)
            height = float(input("And height in feet : ")) /100 * 0.0328084
    print()

    time.sleep(1.5)
    BMI = weight / height**2
    print(f"Your BMI index is {round(BMI, 2)}")

    time.sleep(1)
    print("For adult this BMI range is:")
    time.sleep(0.5)
    if BMI >= 40 :
        print("Obese")
    elif BMI >= 25 :
        print("Overweight")
    elif BMI >= 18.5 :
        print("Normal")
    else:
        print("Underweight")

def info_BMI():
    print()
    time.sleep(0.5)
    print("""What is BMI?
The body mass index or BMI is a ratio of mass to height. It is calculated as kg per square meter or pounds per square inch of height. Numeric BMI values correspond to weight categories including underweight, normal, overweight and obese.

BMI is used as an indicator of the relative healthiness of a person. The Centers for Disease Control (CDC) and the World Health Organization (WHO) recognize that people who are overweight or underweight are at higher risk for certain health conditions. BMI also enables health professionals to discuss bodyweight objectively with their patients.""")

print()
print("-------------------------")
print("For calculate BMI press C")
print("To view info about BMI press I")
inpt = input(": ").lower()
time.sleep(0.5)
match inpt:
    case "c":
        calc_BMI()
    case "i":
        info_BMI()
    case _:
        print("input letter was wrong")
time.sleep(0.5)
print("-------------------------")






