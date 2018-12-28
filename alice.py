# -*- coding: utf-8 -*-
import string
book = open("alice_in_wonderland.txt", "r")

# dict = {}
#
# for lines in book:
#     words = lines.split()
#     for word in words:
#         word = list(word.lower())
#         for letter in word:
#             if letter in string.punctuation:
#                 word = word.replace(letter, " ")
#         word = "".join(word)
#         # print(word)
#         if word in dict:
#             dict[word] += 1
#         else:
#             dict[word] = 1
#
# keyz = sorted(dict.keys())
# # for key in keyz:
# #     print key, dict[key]
#
# valuez = dict.values()
# max = max(valuez)
# print max
#
# print(dict['alice'])

count = {}
longest_word = ""

for line in book:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()
        # print(word)
        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

        if len(word) > len(longest_word):
            longest_word = word

keys = count.keys()
keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")

print("The longest word is", longest_word, "and has", len(longest_word), "letters.")
