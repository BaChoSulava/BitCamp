# Tip Calculator

## კითხვები
1. what fruit is it?
1. how many calories? 
1. რა უნდა გამოიტანოს პროგრამამ პასუხად? / Output / display

## ტექნიკური დავალება
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


### Inputs, Processes, Outputs
არსებითი სახელები:
- name of the fruit/ fruit

ზმნები:
- კითხვა / prompt
- დათვლა / compute
- გამოაჩინოს / display

Item: apple
Proccesses: დათვლა
Calories: 150

### TDD - Test Driven Development - Tests
ტესტის გეგმა #1:
inputs:
    - Apple 
Expected result:
    - Calories: 130  


ტესტის გეგმა #2 - დამრგვალების ტესტი:
inputs:
    - Avocado 
Expected result:
    - Calories: 50

ტესტის გეგმა #3 - დამრგვალების ტესტი:
inputs:
    - Sweet Cherries 
Expected result:
    - Calories: 100

## ფსევდოკოდი - Pseudocode
TipCaluclator
    Initialize fruit

    check what is number of calories

    Display "Calories: {fruit}"
End