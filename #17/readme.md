# Tip Calculator

## კითხვები
1. ჩეკის ოდენობა / bill amount
1. თიფის % / tip rate
1. სრული ოდენობა / total
1. რა უნდა ვკითხოთ იუზერს / Prompt / Input
1. რა უნდა გამოჩნდეს ეკრანზე პროგრამის ჩართვისას? / display
1. რა უნდა გამოიტანოს პროგრამამ პასუხად? / Output / display

## ტექნიკური დავალება
შექმენი მარტივი თიფ კალკულატორი. პროგრამამ უნდა გკითხოს ჩეკის რაოდენობისა და თიფის პროცენტის შესახებ.
პროგრამამ უნდა დათვალოს თიფი და შემდეგ თიფი და სრული ოდენობა გამოიაჩინოს ეკრანზე.

What is the bill? $200
What is the tip percentage? 15
The tip is $30
The total is $230

### Inputs, Processes, Outputs
არსებითი სახელები:
- ჩეკის რაოდენობა / bill amount
- თიფის პროცენტი / tip rate
- თიფი / tip amount
- სრული ოდენობა / total amount

ზმნები:
- კითხვა / prompt
- დათვლა / compute
- გამოაჩინოს / display

Inputs: bill amount, tip rate
Proccesses: დათვლა
Outputs: tip amount, total amount

### TDD - Test Driven Development - Tests
ტესტის გეგმა #1:
inputs:
    - bill amount: 10
    - tip rate: 15
Expected result:
    - Tip: 1.50
    - Total: 11.50


ტესტის გეგმა #2 - დამრგვალების ტესტი:
inputs:
    - bill amount: 11.25
    - tip rate: 15
Expected result:
    - Tip: 1.69
    - Total: 12.94

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