# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# 
# Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:
#
# Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.

import string # has sets of characters to use with 'in' and 'not in'

letters = string.ascii_lowercase + string.ascii_uppercase
strng = """The stump thunk the skunk stunk and the skunk thunk the stump stunk."""

def count(p):
    #count characters, "e", and calc % "e"
    counter = 0
    e = 0
    for char in p:
        if char in letters:
            counter = counter + 1
        if char == "e" or char == "E":
            e = e + 1
    perc = e / counter * 100
    return counter, e, perc
#returns a set
ans = count(strng)
print("Your text contains {} alphabetic characters, of which {} ({:.2}%) are 'e'.".format(ans[0], ans[1], ans[2]))
