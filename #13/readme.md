# Tip Calculator

## კითხვები
1. prompt for name
1. convert to snake style
1. რა უნდა გამოიტანოს პროგრამამ პასუხად? / Output / display

## ტექნიკური დავალება
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

What is the name? firstName
This name in snake style looks like this \ first_name

### Inputs, Processes, Outputs
არსებითი სახელები:
- prompts for the name / name
- snake style / snake_style

ზმნები:
- კითხვა / prompt
- შემოწმება / check
- კონვერტაცია / convert
- გამოტანა / display

Inputs: name
Proccesses: check
Outputs: same , snake style

### TDD - Test Driven Development - Tests
ტესტის გეგმა #1:
inputs:
    - name : firstName
Expected result:
    - This name in snake style looks like this: first_name


ტესტის გეგმა #2 - დამრგვალების ტესტი:
inputs:
    inputs:
    - name : name
Expected result:
    - There is no camel style, so word remains unchanged: name

## ფსევდოკოდი - Pseudocode
convert_to_snake
    input bane
    
    check if not camel then return same

    if camel then convert ro snake

    Display: print returned asnwer
End