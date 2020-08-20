people = 20
cars = 10
trucks = 1

if cars > people or trucks < cars:  ## 如果布尔表达式为真 就运行这个代码
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")

else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars and people < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
