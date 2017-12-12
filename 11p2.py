from fileinput import input
inpt = input("11.txt").readline().strip().split(",")
moves = {"se":0,"n":0,"ne":0}
maxDist,current = 0,0

def calcDistance():
    global moves
    temp = {}
    for key in moves.keys():
        temp[key]=abs(moves[key])
    if temp["se"]<temp["n"]:
        temp["n"]-=temp["se"]
        temp["ne"]+=temp["se"]
        temp["se"]=0
    else:
        temp["se"]-=temp["n"]
        temp["ne"]+=temp["n"]
        temp["n"]=0
    summed = 0
    for key in temp.keys():
        summed+=temp[key]
    return summed

for move in inpt:
    if move in ["se","n","ne"]:
        moves[move]+=1
    elif move=="nw":
        moves["se"]-=1
    elif move=="s":
        moves["n"]-=1
    elif move=="sw":
        moves["ne"]-=1
    current = calcDistance()
    if current>maxDist:
        maxDist = current

print("furthest",maxDist)