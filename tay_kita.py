import math
str = input()
str = str.split(" ")

left = str[:len(str)//2][::-1]
right = str[len(str)//2:]
translation = ""

def word(word):
    word = list(word)
    word_left = word[:len(word)//2][::-1]
    word_right = word[len(word)//2:]
    string = ""
    for i in range(len(word)):
        if i % 2 == 0:
            string += word_right[i//2]
        else:
            string += word_left[i//2]
    return string

for i in range(len(str)):
    if i % 2 == 0:
        translation += word(right[i // 2]) + " "
    else:
        translation += word(left[i // 2]) + " "
print(translation)