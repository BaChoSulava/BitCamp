month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date = input("Date: ")
date_list = date.replace(" ", "/").split("/")

if not date_list[0].isdigit():
    date_list[0] = month.index(date_list[0]) + 1
    print(date_list[0])


new_date = date_list[2] + "-" + f"{date_list[0]:0>2}" + "-" + f"{date_list[1]:0>2}"
print(new_date)

