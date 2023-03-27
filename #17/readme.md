# Tip Calculator

## კითხვები
1. what fruit is it?
1. how many calories? 
1. რა უნდა გამოიტანოს პროგრამამ პასუხად? / Output / display

## ტექნიკური დავალება
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit..


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