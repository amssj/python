def my_while (loops):
    i = 0
    numbers = []
    while i < loops:
        print(f"at the top is {i}")
        numbers.append(i)

        i += 1
        print(f"at the bottom is {i} ")

    print("the numers are")
    for num in numbers:
        print(num)

my_while(4)
