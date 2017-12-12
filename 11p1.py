from fileinput import input
inpt = input("11.txt").readline().strip().split(",")
moves = {"se":0,"n":0,"ne":0}
for move in inpt:
    if move in ["se","n","ne"]:
        moves[move]+=1
    elif move=="nw":
        moves["se"]-=1
    elif move=="s":
        moves["n"]-=1
    elif move=="sw":
        moves["ne"]-=1
for key in moves.keys():
    moves[key]=abs(moves[key])
if moves["se"]<moves["n"]:
    moves["n"]-=moves["se"]
    moves["ne"]+=moves["se"]
    moves["se"]=0
else:
    moves["se"]-=moves["n"]
    moves["ne"]+=moves["n"]
    moves["n"]=0
summed = 0
for key in moves.keys():
    summed+=moves[key]
print("shortest",summed)