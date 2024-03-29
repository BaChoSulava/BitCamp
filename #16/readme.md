# Tip Calculator

## კითხვები
1. what is the plane user wants
1. is it valid or invalid 
1. რა უნდა გამოჩნდეს ეკრანზე პროგრამის ჩართვისას? / display
1. რა უნდა გამოიტანოს პროგრამამ პასუხად? / Output / display

## ტექნიკური დავალება
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
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
is_valid
    input plate

    check for all validation options
    
    if check out then return "valid"
    
    else  "Invalid"

End
