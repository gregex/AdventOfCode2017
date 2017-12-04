number = 289326
xy = [0,0]
stage = 1
known = {(0,0):1}
current = 0

def check():
    global number,current
    if current>number:
        print(current)
        exit()

def add():
    global xy,known,current
    summed = 0
    coords = list(known.keys())
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (xy[0]+i,xy[1]+j) in coords:
                summed += known[(xy[0]+i,xy[1]+j)]
    known[tuple(xy)] = summed
    current = summed
    

while 1:
    check()
    for i in range(stage):
        xy[0]+=1
        add()
        check()
    for i in range(stage):
        xy[1]+=1
        add()
        check()
    stage+=1
    for i in range(stage):
        xy[0]-=1
        add()
        check()
    for i in range(stage):
        xy[1]-=1
        add()
        check()
    stage+=1