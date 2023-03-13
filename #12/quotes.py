quotes = {
        "Oto Zakalashvili" : "სწავლა და ბრძოლა!",
        "Steve Jobs" : "The only way to do great work is to love what you do.",
        "Cory House" : "Code is like humor. When you have to explain it, it’s bad.",
        "Bill Gates" : "Software is a great combination of artistry and engineering.",
        "Albert Einstein" : "It has become appallingly obvious that our technology has exceeded our humanity.",
        }

for names in quotes.keys():
    print(names)
user_inp = input("whose quote do you want to hear? ")
print(f"{user_inp} said \"{quotes[user_inp]}\"")


