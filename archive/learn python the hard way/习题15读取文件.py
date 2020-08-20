from sys import argv

script, filename = argv # 用argv获取文件名

txt = open(filename) ##open命令打开文件

print(f"Here's your file {filename}:")
print(txt.read()) ## 文件本身也有一些给他的命令，接收命令的方式是使用句点

print("Type the filename again:")
file_again = input(" >")

txt_again = open(file_again)
print(txt_again.read())

txt_again.close()

txt.close()


