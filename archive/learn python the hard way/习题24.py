print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n 
the needs of love
not comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")

five = 10 -2 + 3 - 6
print(f"This should be five:{five}") ## 这是一个格式化的字符，把变量放在这几个位置

def secret_formula(started): ## 生成一个名叫secret_formula的函数，参数为started
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars/100
    return jelly_beans, jars, crates ## 返回哪些值

start_point = 10000 ## 设定一个变量 并赋值为10000
beans, jars, crates = secret_formula(start_point) ## 将10000带入函数，返回值赋给三个新的变量

print("With a starting point of :{}".format(start_point)) ## 这是一个格式化的字符 变量放在这借个位置
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point) ##将生成的函数赋值给formula变量

print("We'd have {} beans, {} jars, and {} cartes.".format(*formula)) ## 将变量的带入，注意* 他高速python把函数的所有参数都接收进来，然后放到formula中。
