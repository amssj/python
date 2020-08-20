from sys import argv

script, filename = argv

print("we are going to erase the content in the ex16")
print("If you want me to do that, please press return")
print("If not, please press CTRL-C(^C).")

input("?")

print("Opening the file")
target = open(filename,'w')
print("I have truncate the content in the ex16")
target.truncate()
print("Now I will rewrite some stuff on the ex16")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")


target.write(line1)
target.write(line2)
target.write(line3)

print("finally, we close it")
target.close()
