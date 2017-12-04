from fileinput import input
data = input("input.txt")
count = 0
for row in data:
    words = row.strip().split(" ")
    if len(words)==1:
        continue
    setOfwords = set(words)
    if len(words)==len(setOfwords):
        count+=1
print(count)