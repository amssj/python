## 文档字符串
def func(x,y):
    '''Prints the maximum of two numbers.
    
    The two values must be integers'''
    x = int(x)
    y = int(y)
    if x < y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
print(func(3,5))
print(func.__doc__)
