from fileinput import input

data = input("12.txt")
connections = {}
count = 0

def findSet(key):
    global connections,count
    findMe = key
    track  = [key]
    oldTrack = []
    while True:
        for key in connections.keys():
            track.extend([x for x in connections[key] if key in track])
        if len(oldTrack) == len(set(track)):
            break
        else:
            oldTrack = set(track)
    for elem in set(track):
        del connections[elem]
    count += 1

for row in data:
    splited = row.strip().split(" <-> ")
    connections[int(splited[0])] = tuple([int(x) for x in splited[1].split(", ")])

while len(connections.keys()):
    findSet(list(connections.keys())[0])
print(count)