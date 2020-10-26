# coding=utf-8

def ngram(n, lst):
    return zip(*[lst[i:] for i in range(n)])


str = 'I am an NLPer'
splits = str.split()

words_bi_gram = ngram(2, splits)
chars_bi_gram = ngram(2, str)

print(words_bi_gram)
print(chars_bi_gram)

str1 = 'paraparaparadise'
str2 = 'paragraph'
X = set(ngram(2,str1))
Y = set(ngram(2,str2))

union = X | Y
intersection = X & Y
difference = X - Y

print('X:', X)
print('Y:', Y)
print(u"和集合:", union)
print(u'積集合:', intersection)
print(u'差集合:', difference)
print(u'Xにseが含まれるか:', {('s', 'e')} <= X)
print(u'Yにseが含まれるか:', {('s', 'e')} <= Y)

def cipher(str):
    rep = [chr(219 - ord(x)) if x.islower() else x for x in str]
    #rep = [chr(219 - ord(x)) if x.islower() else x for x in str]
    return ''.join(rep)

message = 'the quick brown fox jumps over the lazy dog'
message = cipher(message)
print(message)
message = cipher(message)
print(message)

import random

def shuffle(str):
    result = []
    for word in str.split():
        if len(word) > 4:
            word = word[:1] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1:]
        result.append(word)
    return ' '.join(result)

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = shuffle(str)
print(ans)

import random

def shuffle(words):
    result = []
    for word in words.split():
        if len(word) > 4:  # 長さが4超であればシャッフル
            word = word[:1] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1:]
        result.append(word)
    
    return ' '.join(result)

words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = shuffle(words)

print(ans)
