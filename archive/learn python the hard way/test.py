from sys import exit  # 引入 sys 部分模块 exit


def gold_room():  # 定义函数 gold_room
    print("This room is full of gold. How much do you take?")  # 打印字符串

    choice = input(" > ")  # 输出提示信息">"，接收输入内容，并将输入的内容赋值给变量 choice
    if "0" in choice or "1" in choice:  # 如果变量 choice 的值为 0 或者 1
        how_much = int(choice)  # 调用 int()函数，将变量 choice 的值转换为整型，并赋值给变量 how_much
    else:  # 如果变量 choice 的值不是 0 或 1
        dead("Man, learn to type a number.")  # 调用 dead() 函数,打印字符串

    if how_much < 50:  # 如果变量 how_much 的值小于 50
        print("Nice, you're not greedy, you win!")  # 打印字符串
        exit(0)  # 程序正常退出
    else:  # 如果 if 后面的条件语句为 False ，则判断 elif 后面的条件语句,若为 True，则调用 dead() 函数
        dead("You greedy bastard!")  # 调用 dead() 函数,打印字符串


def bear_room():  # 定义函数 bear_room
    print("There is a bear here.")  # 打印字符串
    print("The bear has a bunch of honey.")  # 打印字符串
    print("The fat bear is in front of another door.")  # 打印字符串
    print("How are you going to move the bear?")  # 打印字符串
    bear_moved = False  # 将布尔值 False 赋值给变量 bear_moved

    while True:  # 判断布尔表达式的真假,如果为 True,则一直循环直到表达式为False为止
        choice = input(" > ")  # 输出提示信息">"，接收输入内容，并将输入的内容赋值给变量 choice

        if choice == "Take honey":  # 如果变量 choice 等于 "Take money"
            dead("The bear looks at you then slaps your face off.")  # 调用 dead() 函数，打印字符串
        elif choice == "taunt bear" and not bear_moved:  # 如果 if 后面的条件语句为 False ，则判断 elif 后面的条件语句,若为 True，则打印以下字符串并将布尔值 True 赋值给变量 bear_moved
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:  # 如果 if 后面的条件语句为 False ，则判断 elif 后面的条件语句,若为 True，则调用 dead() 函数并打印字符串
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:  # # 如果 if 后面的条件语句为 False ，则判断 elif 后面的条件语句,若为 True，则调用 gold_room() 函数
            gold_room()
        else:  # 若if和elif后面的条件语句都是为False, 则打印else后面的字符串
            print("I got no idea what that means.")


def cthulhu_room():  # 定义函数 cthulhu_room
    print("Here you see the great evil Cthulhu.")  # 打印字符串
    print("He, it, whatever stares at you and you go insane.")  # 打印字符串
    print("Do you flee for your life or eat your head?")  # 打印字符串

    choice == input(" > ")  # 输出提示信息">"，接收输入内容，并将输入的内容赋值给变量 choice

    if "flee" in choice:  # 如果变量 choice 的值为 flee
        start()  # 调用 start() 函数
    elif "head" in choice:  # 如果变量 choice 的值为 head
        dead("Well that was tasty!")  # 调用 dead() 函数并打印字符串
    else:  # 如果两者都不是则调用 cthulhu_room 函数
        cthulhu_room()


def dead(why):  # 定义函数 dead() ，位置参数为 why
    print(why, "Good job!")  # 打印字符串
    exit(0)  # 程序正常退出


def start():  # 定义函数 start()
    print("You are in a dark room.")  # 打印字符串
    print("There is a door to your right and left.")  # 打印字符串
    print("Which one do you take?")  # 打印字符串

    choice = input(" > ")  # 输出提示信息">"，接收输入内容，并将输入的内容赋值给变量 choice

    if choice == "left":  # 如果变量 choice 的值为 left
        bear_room()  # 调用 bear_room 函数
    elif choice == "right":  # 如果变量 choice 的值为 right
        cthulhu_room()  # 调用 cthulhu_room 函数
    else:  # 如果两者都不是则调用 dead() 函数并打印字符串
        dead("You stumble around the room until you starve.")


start()  # 调用函数 start() 游戏开始
