from sys import exit
from sys import argv

def start():
    print("""there'r three doors in front of you 
          \n\thow do you choose?""")
    print("-----------------------")
    choose = input("""
        1,monster
        2,white
        3,wisdom
        >""")
    if choose == "1":
        monster()
    elif choose == "2":
        white()
    elif choose == "3":
        wisdom()
    else:
        dead("you should choose in these chooses")

def dead(note):
    print(note,"dear~")
    exit(0)

def monster():
    print("""Now you see the moster \n
    haha, hope it does not scare you\n
    \t\t\t/(ㄒoㄒ)/~~
    you should make some calculations
    if you are right, you will pass, or else, you must do it again and again O(∩_∩)O""")
    monster_remain = False
    print("\t\t5 + 6/3 + 3 * 4 - (34*2 + 22/2)")


    while True:
        print("---------------------------------")
        answer = input("\tplease input your answer >")

        if answer == "-9" and not monster_remain:
            print("Wow,You are brilliant you can pass")
            gold()
        elif answer == "9" and not monster_remain:
            print("it seems you answer wrong")
            print("but the monster forgive you")
            gold()
        else:
            print("I have no idea about what you're doing")
        exit(0)

def gold():
    print("-----------------------------")
    print("Now you will see the gold")
    print("Do you want to take some away")
    print("Let's play a guessing game~~~")

    print("""
    Now I write a number on the paper
    can you guess it
    you have only three chance""")
    print("\n\t\t A hint: it is less than 10")

    count = 0
    while count < 3:
        math = int(input("please input your number <"))
        if math == 5:
            print("you are genies")
            print("you can take as much as you want")
            exit(0)
        else:
            print("you'r wrong,dear")
        count = count + 1
    else:
        dead("it is a pity")


def white():
    print("let's read a poem")
    print("-----------------")
    print("""
    \tI love you, princess
\t\tYou are like the star in the sky
\t\t\tThe fish in the river
\t\t\tI hope I can serve you forever
""")
    print("-----------------")
    print("you have done very well")
    gold()

def wisdom(started):
    star = input("please input a number randomly")
    red = started * 10
    black = red + 20
    blue = black/23
    return red,black,blue
    print("With a star point of {}".format(star))
    print(f"We'd have {red} beans,{black} jars,and {blu} crates")




start()








