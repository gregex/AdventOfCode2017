from fileinput import input

data = input("12.txt")
connections = {}

def findSet(key):
    global connections
    findMe = key
    track  = [key]
    oldTrack = []
    while True:
        for key in connections.keys():
            track.extend([x for x in connections[key] if key in track])
        if len(oldTrack) == len(set(track)):
            return len(oldTrack)
        else:
            oldTrack = set(track)

for row in data:
    splited = row.strip().split(" <-> ")
    if splited[0] == splited[1]:
        continue
    else:
        connections[int(splited[0])] = tuple([int(x) for x in splited[1].split(", ")])

print(findSet(0))