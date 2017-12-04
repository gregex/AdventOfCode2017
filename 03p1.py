number = 289326
xy = [0,0]
stage = 1
current = 1

def check():
    global number,current,xy,stage
    if number==current:
        print(abs(xy[0])+abs(xy[1]))
        exit()

while 1:
    check()
    for i in range(stage):
        xy[0]+=1
        current+=1
        check()
    for i in range(stage):
        xy[1]+=1
        current+=1
        check()
    stage+=1
    for i in range(stage):
        xy[0]-=1
        current+=1
        check()
    for i in range(stage):
        xy[1]-=1
        current+=1
        check()
    stage+=1