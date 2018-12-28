#.count()
def county(lst, target):
    count = 0
    for element in lst:
        if element == target:
            count += 1
    print(count)

lst1 = ["Jen", "Mike", "Mary", "Tim"]
lst2 = ["Sam", "Mike", "Mary", "Jen"]
lst3 = ["Jen", "Sam", "Mary", "Sam"]

#county(lst1, "Sam")
#county(lst2, "Sam")
#county(lst3, "Sam")

#.in()
def in_there(lst, target):
    there = False
    for element in lst:
        if element == target:
            there = True
    print(there)

#in_there(lst1, "Sam")
#in_there(lst2, "Sam")
#in_there(lst3, "Sam")

#.reverse()
def reverser(lst):
    reversed = []
    for index in range(len(lst)):
        reversed.append(lst.pop())
    print(reversed)

reverser(lst1)


#.index()
def indexer(lst, target):
    indx = -1
    indx_count = 0
    for i, element in enumerate(lst):
        if indx_count == 1:
            break
        if element == target:
            indx = i
            indx_count += 1
    print(indx)


#indexer(lst1, "Sam")
#indexer(lst2, "Sam")
#indexer(lst3, "Sam")

#.insert()
def inserter(lst, target, indx):
    j = 0
    temp_list = [None] * (len(lst) + 1)
    for i in range(indx):
        temp_list[i] = lst[i]
        j += 1
    temp_list[indx] = target
    j += 1
    for i in range(j, len(lst) + 1):
        temp_list[i] = lst[i - 1]
    print(temp_list)




inserter(lst1, "Bob", 2)
