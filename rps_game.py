import random
from secrets import choice

choice_list = ['rock', 'paper', 'scissor']
choices = 0
upoints = 0
cpoints = 0


while True:
    press = int(input("""
        press 1. start
        press 2. exit """))

    if (press == 1):

        while choices < 5:

            uinput = int(input("""
                1 for rock
                2 for paper
                3 for scissor"""))

            if (uinput == 1) or (uinput == 2) or (uinput == 3):

                if uinput == 1:
                    uinput = "rock"

                elif uinput == 2:
                    uinput = "paper"
                    print("you selected paper")
                    cinput = random.choice(choice_list)
                    print(cinput)

                elif uinput == 3:
                    uinput = "scissor"

                cinput = random.choice(choice_list)
                print = ("user input")
                print = ("computer input")
                choices = choices+1

                """   if ((uinput == "rock") and (cinput == "scissor")) or ((uinput == "paper") and (cinput == "rock")) or ((uinput == "scissor") and (cinput == "paper")):
                        print("user win")
                        upoints = upoints+1 """

                """   elif ((cinput == "rock") and (uinput == "scissor")) or ((cinput == "paper") and (uinput == "rock")) or ((cinput == "scissor") and (uinput == "paper")):
                        print("computer win")
                        cpoints = cpoints+1 """

            else:
                print("invalid input")
                continue

    else:
        break
