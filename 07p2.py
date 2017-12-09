from fileinput import input
data = input("tree.txt")
relations = {}
weights = {}
groupWeights = {}
levels = {}
every = []

def calculateLevels(key):
    global relations
    level = 0
    for value in list(relations.values()):
        if key in value:
            level += 1
            wantedKey = list(relations.keys())[list(relations.values()).index(value)]
            #wantedKey = x for x,y in relations.items() if y==value
            level += calculateLevels(wantedKey)
    return level

def branchWeight(leaf):
    global relations,weights
    summed = weights[leaf]
    if leaf not in list(relations.keys()):
        return summed
    for kid in list(relations[leaf]):
        summed += branchWeight(kid)
    return summed

for row in data:
    splited = row.split(" ")
    weights[splited[0]] = int(splited[1].strip()[1:-1])
    if "->" in splited:
        parent = splited[0]
        kids = []
        index = splited.index("->")
        for i in range(index+1,len(splited)):
            kids.append(splited[i].strip().strip(',').strip('\n'))
        relations[parent] = tuple(kids)

for parent in list(relations.keys()):
    groupWeights[parent] = branchWeight(parent)

maxLvl = 0
for kid in list(weights.keys()):
    levels[kid] = calculateLevels(kid)
    if levels[kid]>maxLvl:
        maxLvl=levels[kid]

for i in range(0,maxLvl+1):
    print("Level",i)
    for leaf in list(relations.keys()):
        if levels[leaf]==i:
            allBws = []
            bws = {}
            for kid in list(relations[leaf]):
                if kid not in list(relations):
                    bws[kid] = weights[kid]
                    allBws.append(weights[kid])
                else:
                    bws[kid] = groupWeights[kid]
                    allBws.append(groupWeights[kid])
            if(len(set(allBws))==1):
                continue
            culprit = list(bws.keys())[list(bws.values()).index(min(allBws,key=allBws.count))]
            allBws.remove(bws[culprit])
            delta = bws[culprit]-allBws[0]
            print(culprit,relations[culprit])
            print(weights[culprit]-delta)