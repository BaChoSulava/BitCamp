import datetime
from datetime import date, datetime, timedelta
import sys
import inflect


def main():
    birthday = get_date()
    age_in_minutes(birthday)

def get_date():
    birth_date = input("Date of Birth: ")
    formated_date = birth_date.strip().split("-")
    try:
        for i in formated_date:
            i.isdigit()
    except:
        sys.exit("Invalid date")
    
    if len(formated_date[0]) != 4 and len(formated_date[1]) != 2 and len(formated_date[2]) != 2:
        sys.exit("Invalid date")
    return formated_date

def age_in_minutes(birthday):
    today = date.today()
    user_birthdate = date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
    age = today - user_birthdate
    age_in_minutes = round(age.total_seconds() / 60)

    p = inflect.engine()
    age_str = p.number_to_words(age_in_minutes) + " minute"
    if age_in_minutes != 1:
        age_str += "s"

    print("{}".format(age_str))
    

if __name__ == "__main__":
    main()