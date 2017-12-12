from fileinput import input
data = input("4.txt")
countUnfit = {}
countRows = 0
total = 0

for row in data:
    countRows+=1
    countUnfit[countRows] = 0
    words = row.strip().split(" ")
    for i in range(len(words)):
        for j in range(min((i+1),len(words)),len(words)):
            first = list(words[i])
            second = list(words[j])
            first.sort()
            second.sort()
            if first==second:
                countUnfit[countRows]+=1
for value in list(countUnfit.values()):
    if value==0:
        total+=1
print(total)
