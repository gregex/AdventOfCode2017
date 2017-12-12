from fileinput import input

data = input("9.txt")
summed = 0
layer = 0

for row in data:
    row=row.strip()

i = 0
noExc = ""
while i<len(row):
    if row[i]=='!':
        i+=2
    else:
        noExc+=row[i]
        i+=1

i = 0
noGarbage = ""
while i<len(noExc):
    if noExc[i]=="<":
        while noExc[i]!=">":
            i+=1
    else:
        noGarbage+=noExc[i]
    i+=1

i = 0
while i<len(noGarbage):
    if noGarbage[i]=="{":
        layer+=1
    elif noGarbage[i]=="}":
        summed += layer
        layer -= 1
    i+=1
print(summed)
