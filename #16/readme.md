# Tip Calculator

## კითხვები
1. what is the plane user wants
1. is it valid or invalid 
1. რა უნდა გამოჩნდეს ეკრანზე პროგრამის ჩართვისას? / display
1. რა უნდა გამოიტანოს პროგრამამ პასუხად? / Output / display

## ტექნიკური დავალება
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

What do you want written on the plate? cs50
it's Valid
or
it's Invalid

### Inputs, Processes, Outputs
არსებითი სახელები:
- inputed plate / plate
- valid or not / is_valid

ზმნები:
- კითხვა / prompt
- check for validation 
- გამოაჩინოს / display


### TDD - Test Driven Development - Tests
ტესტის გეგმა #1:
inputs:
    - Plate: CS50
Expected result:
    - Valid

ტესტის გეგმა #2 - დამრგვალების ტესტი:
inputs:
    - Plate: CS05
Expected result:
    - Invalid

ტესტის გეგმა #3 - დამრგვალების ტესტი:
inputs:
    - Plate: CS50P
Expected result:
    - Invalid


ტესტის გეგმა #4 - დამრგვალების ტესტი:
inputs:
    - Plate: PI3.14
Expected result:
    - Invalid


ტესტის გეგმა #5 - დამრგვალების ტესტი:
inputs:
    - Plate: H
Expected result:
    - Invalid


ტესტის გეგმა #6 - დამრგვალების ტესტი:
inputs:
    - Plate: OUTATIME
Expected result:
    - Invalid


## ფსევდოკოდი - Pseudocode
TipCaluclator
    Initialize billAmount to 0
    Initialize tip to 0
    Initialize tipRate to 0
    Initialize total to 0

    Prompt for billAmount with "What is the bill amount?"
    Prompt fot tipRate with "What is the tip rate?"

    convert billAmount to a number
    covnert tipRate to a number

    tip = billAmount * (tipRate / 100)
    round tip up to nearest cent
    total = billAmount + tip

    Display "Tip: $" + tip
    Display "Total: $" + total
End