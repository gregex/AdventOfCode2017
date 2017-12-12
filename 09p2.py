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
while i<len(noExc):
    if noExc[i]=="<":
        i+=1
        while noExc[i]!=">":
            i+=1
            summed+=1
    i+=1

print(summed)
