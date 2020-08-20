number = 34
running = True

while running:
        guess = int(input('please enter a world:'))
        if guess == number:
            print("congrulations")
            running = False
        elif guess < number:
            print("No,it is a little lower than that")
        else:
            print("No,it is a little higher than that")
else:
    print('The while loop is over')
