# განსხვავებუი მისალმებებით
import random
hellos = ["გამარჯობა ",
          "მოგესალმები ",
          "გაუმარჯოს ",
          "ბარო ",
          "Nice to meet you ",
          "Hello "
          ]

def say_hi():
    name = input("What is your name? : ").strip().title()   #ჭრის ცარიელ ადგილებს სტრინგის თავში და ბოლოში. ასევე ვიზუალს უცვლის სტრინგს.
    name = name.split()                                     #იყოფა სტრინგი სიტყვებად, რის შედეგად უქმდება სიტყვებს შორის ცარიელი ადგილები.
    name = set(name)                                        #უქმდება დუბლირებული სიტყვები.
    name = ' '.join(name)                                   #აერთიანებს მიღებულ სიას ერთ სტრინგად.
    print(random.choice(hellos) + name + "!")               #იბეჭდება შედეგი.


say_hi()
