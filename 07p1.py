from fileinput import input
data = input("7.txt")
relations = {}

def isIn(key):
    global relations
    for value in list(relations.values()):
        if key in value:
            return 1
    return 0

for row in data:
    splited = row.split(" ")
    if "->" in splited:
        parent = splited[0]
        kids = []
        index = splited.index("->")
        for i in range(index+1,len(splited)):
            kids.append(splited[i].strip().strip(',').strip('\n'))
        relations[parent] = tuple(kids)

for key in list(relations.keys()):
    if not isIn(key):
        print(key)
