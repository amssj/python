def print_two(*args): ## 使用def创建一个函数
    arg1, arg2 = args ##将函数解包
    print(f"arg1: {arg1},arg2:{arg2}")## 将解包后的参数打印出来

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
