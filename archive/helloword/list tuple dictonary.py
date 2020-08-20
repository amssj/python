## This is my shopping list
shoplist = ['box','pen','cloth','umbrella','gift']
print('I want to buy',len(shoplist),'items')
print('The items are',end=" ")
for item in shoplist:
        print(item,end=' ')
print("\n I also want to buy")
shoplist.append('apple')
print('my shoplist is now',shoplist)

print('I will sort my shoplist')
shoplist.sort()
print('sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])
del shoplist[0]
print('my shoplist is now',shoplist)

###Tuple

zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))

new_zoo = ('Monkey','Camel',zoo)
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)

print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))

## dir
ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Masumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}

## swaroop的地址是什么
print("Swaroop's address is",ab['Swaroop'])

## 删除spammer及其地址 看一下addressbook中有哪些地址，进而轮番打印每一个地址。
del ab['Spammer']
print('There are {} address in the ab'.format(len(ab)))
for name,address in ab.items():
    print("contact {} at {}".format(name,address))
##增加新的地址

ab["Liushujun"] = 'liushujun@163.com'
if "Liushujun" in ab:
    print("Liushujun's address is",ab['Liushujun'])

## 序列
shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Item -3 is',shoplist[-3])
print('Item 0 is',name[0])

## slicing on a list

print('Item 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])

## sling on a string
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -1 is',name[1:-1])
print('characters start to end is',name[:])

## step
shoplist = ["apple","mango","carrot","banana"]
print('items are',shoplist[::1])
print('items are',shoplist[::2])
print('items are',shoplist[::3])
print('items are',shoplist[::-1])
