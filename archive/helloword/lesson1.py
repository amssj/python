## 变量与常量
i = 5
print(i)
i = i + 1
print(i)
s = ''' this is the first line.\n this is the second line.'''
print(s)
## 物理行与逻辑行 不常用，如果想要
s = 'this is a string.\
this continues the string.'
print(s)
a = "I must work very hard to prove myself and for a better life.\n however, what I said is not the reality"
print(a)
print(4 + 3)
print(3 * 5)
##字符串乘以3 表示三次输出la
print("la" * 3)
## 表示3的4次方
print(3 ** 4)
## /表示除法 //表示整除
## % 表示取模（余数）
print(13 % 3)
## & 表示按位与
## | 表示按位或
## ^ 表示按位异
## ~ 表示按位取反
a = 2
a = a * 3  # a * = 3
print(a)
## 表达式
length = 5
breadth = 2
area = length * breadth
print("Area is ", area)
print("Perimerter is", 2 * (length + breadth))
## while语句

number = 23
running = True

while True:
    ##猜测数
    guess = int(input('Enter an integer:'))
    ##猜测数如果等于number
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number :
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over')
print('Done')
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('too small')
        continue
    print('Input is of sufficient length')

##function
def print_max(a,b):
    if a > b:
        print(a,"is maximum")
    elif a == b:
        print(a,"is equal to",b)
    else:
        a < b
        print(b,"is maximum")

print_max(32,45)

## continue

while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('too small')
        continue
    print('Input is of sufficient length')

##local variable
x=50

def func(x):
    print("x is ",x)
    x=2
    print("change local x to",x)
func(x)
print('x is still',x)

##default
def say(message,times=1):
    print(message * times)

say('hello')
say("python",5)

## keyword argument
def func(a,b=5,c=10):
    print("a is",a,"and b is",b,"and c is",c)
func(3,8)
func(25,c=24)
func(c=50,a=43)


## returen
def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return "the numbers are equal "
    elif x < y:
        return y
print(maximum(2,3))
