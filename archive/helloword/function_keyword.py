##  keyword argument
def func(a,b=5,c=10):
    print("a is",a,"and b is",b,"and c is",c)
func(3,8)
func(25,c=24)
func(c=50,a=43)
