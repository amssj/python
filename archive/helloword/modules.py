## modules 如果你想在所编写的别的程序中重用一些函数
import sys ## 告诉python希望使用这一模块

print('The command line arguments are:')
for i in sys.argv:##sys.argv变量是一系列字符串的列表
    print(i)

print('\n\nThe PYTHONPATH is', sys.path,'\n')

##模块的__name__
if __name__== '__main__':##每一个模块都定义了它的__name__属性，如果它与__main__属性相同，则代表这一模块是由用户独立运行的。
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

## 导入自己的模块
import mymodule

mymodule.mymodule()

print('version',mymodule.__version__)
