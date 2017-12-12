from fileinput import input

jumps = [int(elem.strip()) for elem in input("5.txt")]
jumpLen = len(jumps)
i, count = 0,0

while i<jumpLen and i>=0:
        old = jumps[i]
        jumps[i] += 1
        i += old
        count += 1

print(count)
