entry = [int(x) for x in "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6".split("\t")]
count = 0
seen = []

while 1:
    seen.append(tuple(entry))
    index = entry.index(max(entry))
    value = entry[index]
    entry[index] = 0
    while value:
        index += 1
        index %= len(entry)
        entry[index] += 1
        value -= 1
    count += 1
    if tuple(entry) in seen:
        print(count)
        exit()