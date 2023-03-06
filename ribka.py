import collections
n = int(input())
def up_dict(num):
    dict = {}
    for i in range(num):
        limit = input().split(" ")
        dict[limit[0]] = int(limit[1])
    return dict
first_word = ""
last_word = ""
for i in range(n):
    word = input()
    first_word += word[0]
    last_word += word[-1]

first_letter, last_letter = up_dict(int(input())), up_dict(int(input()))
first_collec, last_collec = collections.Counter(first_word), collections.Counter(last_word)
first_count, last_count = 0, 0
word_count1 = sum([min(first_letter.get(i), first_collec.get(i)) for i in first_letter.keys() if first_collec.get(i) != None])
word_count2 = sum([min(last_letter.get(i), last_collec.get(i)) for i in last_letter.keys() if last_collec.get(i) != None])
print(min(word_count2, word_count1))
