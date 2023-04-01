names = []

while True:
    try:
        prompt = input("Name: ")
        if prompt == "q":
            break 
        names.append(prompt)
    except EOFError:
        break

if len(names) >=2:
    Adieu = ", ".join(names[:-1])
    print(f"Adieu, adieu, to {Adieu} and {names[-1]}")
if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")