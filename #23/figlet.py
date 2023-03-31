from pyfiglet import Figlet
import random

figlet = Figlet()

#learn what user want to do with text
while True:
    text_type = input("text type: ")
    splited_text_type = text_type.split()
    print(splited_text_type)
    if len(splited_text_type) == 0 or len(splited_text_type) == 2:
        break

#inut text that will be changed
text = input("text input: ")

#otpions:
font_type = ''
if len(splited_text_type) == 0:
    font_type = random.choice(figlet.getFonts())
    print(font_type)
else:
    if splited_text_type[0] != "-f" and splited_text_type[0] != "--font":
        print("error writing '-f' or '--font'")
    elif not splited_text_type[1] in figlet.getFonts():
        print("error spelling font-type")
    else:
        font_type = splited_text_type[1]

figlet.setFont(font=font_type)
print(figlet.renderText(text))

    

