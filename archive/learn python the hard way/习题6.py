types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said :{x}") ##把一个字符串放到另一个字符串里
print(f"I also said :'{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious)) ##当在已经创建的字符串上应用格式的时候

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)



