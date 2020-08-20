types_of_people = 10 ##变量赋值
x = f"There are {types_of_people} types of people." ## 这是一个格式化的字符串，其中插入变量
binary = "binary"
do_not = "don't"
y = f"Those who know binary and those who do_not"
print(x)
print(y)
print(f"I said:{x}")
print(f"I also said:'{y}")

hilarious = False ## 变量赋值
joke_evaluation = "Isn't that joke so funny?!{}" ## 笑话是否好笑赋值

print(joke_evaluation.format(hilarious)) ## 以format的形式打印

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)


