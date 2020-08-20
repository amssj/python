def cheese_and_crackers(cheese_count,boxes_of_crackers): ## 生成函数 设定参数
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30) ## 可以直接给参数赋数值

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50 ## 可以将变量作为参数

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6) ## 可以在函数参数内进行计算

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000) ## 变量和数字的运算也可以作为参数

