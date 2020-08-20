## function_global


x=50
def func():
    global x
    print("x is",x)
    x=2
    print("change global x to",2)
func()
print("value of x is ", x)
