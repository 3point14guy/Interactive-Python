import string #has sets of characters to use with 'in' and 'not in'

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
