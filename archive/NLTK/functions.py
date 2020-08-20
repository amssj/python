#function 这一项目可以任意调用这里的函数

def plural(word):
    if word.endswith('y'):
        return word[:-1]+'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh','ch']:
        return word +'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

print(plural('fairy'))
print(plural('woman'))

###模块
