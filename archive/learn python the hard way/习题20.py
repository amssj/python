## 将函数与文件相结合
sudo apt install python3-pip
from sys import argv ## 引出并使用argv获取文件名

script, input_file = argv

def print_all(f): ## 生成函数名为print_all的函数，f是一个变量，在这里指的是一个文件
    print(f.read())

def rewind(f): ## 生成函数名为rewind的函数，f是一个变量，在这里指的是一个文件
    f.seek(0) ## 每次运行seek就回到了文件开始的地方

def print_a_line(line_count,f): ## 生成函数名为print_a_line的函数
    print(line_count,f.readline()) ## readline（）里面的代码会扫描文件的每一个字节，直到找到一个\n为止，停止读取文件并返回此前文件发现的内容。

current_file = open(input_file)##将开始input_file赋值给current_file

print("First let's print thpye whole file:\n") ## 打印整个文件，并空格

print_all(current_file)## 动用print_all函数

print("Now let's rewind,kind of like a tape.")

rewind(current_file)## 动用rewind函数


print("Let's print three line:")

current_line = 1
print_a_line(current_line, current_file) ## 动用print_a_line 函数

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
