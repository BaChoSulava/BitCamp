# Tip Calculator

## კითხვები
1. prompt text
1. რა უნდა გამოჩნდეს ეკრანზე პროგრამის ჩართვისას? / display
1. what is Output / display

## ტექნიკური დავალება
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

whire text? twitter

### Inputs, Processes, Outputs
არსებითი სახელები:
- inputed text / text
- output text / out_text

ზმნები:
- input text
- omitt vowels
- display result

Inputs: twitter
Proccesses: find vowels
Proccesses: cut them out
Outputs: twttr

### TDD - Test Driven Development - Tests
ტესტის გეგმა #1:
inputs:
    - text: Twitter 
Expected result:
    - omitted: Twttr


ტესტის გეგმა #2 - დამრგვალების ტესტი:
inputs:
    - text: What's your name? 
Expected result:
    - omitted: Wht's yr nm?

ტესტის გეგმა #3 - დამრგვალების ტესტი:
inputs:
    - text: CS50
Expected result:
    - omitted: CS50

## ფსევდოკოდი - Pseudocode
ommit_vowels

    enter text

    check every word for vowels

    cut them out

    dispay new word

End