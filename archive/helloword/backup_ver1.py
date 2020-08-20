class Pearson:
    pass
p = Pearson()
print(p)

class Person:
    def say_hi(self):
        print("Hello,how are you?")
p = Person()
p.say_hi()

class Person:
    def _init_(self,name):
        self.name = name
    def say_hi(self):
        print("Hello,my name is",self.name)
p = Person('Swaroop')
p.say_hi()
