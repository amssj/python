## 字符串的更多内容 name.startwith; in; name.find; delimiter.join
name = "Swaroop"

if name.startswith("Swa"):
    print("Yes, the string starts with 'Swa' ")

if 'a' in name:
    print("Yes, it contains the string 'a'")

if name.find('war') != -1:
    print("Yes, it contains the string 'war'")

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print(delimiter.join(mylist))

