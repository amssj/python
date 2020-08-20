def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') ##
    return words

def sort_words(words):
    """Sorts the words.""" ### 对list进行排序 sort是在原位重新排列列表 sorted产生一个新的列表
    return sorted(words)

def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0) ## pop（）指定删除对象的索引位置
    print(word)

def print_last_word(words):
    """Prints the last word after poping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentenceand returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

