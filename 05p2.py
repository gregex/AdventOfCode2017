from fileinput import input

jumps = [int(elem.strip()) for elem in input("jumps.txt")]
jumpLen = len(jumps)
i, count = 0,0

while i<jumpLen and i>=0:
        old = jumps[i]
        if(jumps[i]>=3):
            jumps[i] -= 1
        else:
            jumps[i] += 1
        i += old
        count += 1

print(count)