# for i in range(1, 13):
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}"
#         .format(i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))

# def reverse(astring):
#     # reversed = [None] * len(astring)
#     reversed = []
#     for i in range(len(astring)):
#         j = len(astring) - 1 - i
#         reversed.append(astring[j])
#     print ''.join(reversed)
# reverse("pickle")


# def remove_letter(theLetter, theString):
#     a = theString.find(theLetter)
#     while a != -1:
#         theString = theString[:a] + theString[a+1:]
#         a = theString.find(theLetter)
#     print(theString)
#
# remove_letter("a", "banana")
