# Tip Calculator

## კითხვები
1. amount due
1. is it at least 50 cents
1. if not how many is due
1. how many is a change

## ტექნიკური დავალება
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output at least 50 cents. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


### Inputs, Processes, Outputs
არსებითი სახელები:
- amount inserted each time/ coin
- Amount Due / amount_due
- change to return / change_owed

ზმნები:
- prompt to insert coin 
- check for amount
- calc hole amount
- calc Amount Due
- calc change
- display due
- display answer

### TDD - Test Driven Development - Tests
ტესტის გეგმა #1:
inputs:
    - Insert Coin : 25
Expected result:
    - Amount Due: 25
    - contiue prompt


ტესტის გეგმა #2 - დამრგვალების ტესტი:
inputs:
    inputs:
    - Insert Coin : 10
Expected result:
    - Amount Due: 40
    - contiue prompt

ტესტის გეგმა #3 - დამრგვალების ტესტი:
inputs:
    inputs:
    - Insert Coin : 5
Expected result:
    - Amount Due: 45
    - contiue prompt

ტესტის გეგმა #4 - დამრგვალების ტესტი:
inputs:
    inputs:
    - Insert Coin : 30
Expected result:
    - Amount Due: 50
    - contiue prompt
'''because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.'''

ტესტის გეგმა #5 - დამრგვალების ტესტი:
inputs:
    inputs:
    - Insert Coin : 25
    - Insert Coin : 25
Expected result:
    - Change Owed: 0
    - contiue prompt

ტესტის გეგმა #6 - დამრგვალების ტესტი:
inputs:
    inputs:
    - Insert Coin : 25
    - Insert Coin : 10
    - Insert Coin : 25
Expected result:
    - Change Owed: 10
    - contiue prompt


## ფსევდოკოდი - Pseudocode
coke_mashine

    input coin
    
    check if not in axcaptable coin range
    
    if not in range make coin value 0
    
    sum all given coins
    
    if above 50 then calc owed display it 

    if not above 50 then calc due and display it

End