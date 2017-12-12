from fileinput import input
data = input("8.txt")
variables = {}

def compare(x,y,sign):
    if sign=="==":
        return x==y
    elif sign=="<=":
        return x<=y
    elif sign==">=":
        return x>=y
    elif sign==">":
        return x>y
    elif sign=="<":
        return x<y
    elif sign=="!=":
        return x!=y

for row in data:
    splited = row.strip().split()
    if splited[4] not in variables:
        variables[splited[4]] = 0
    if compare(variables[splited[4]],int(splited[6]),splited[5]):
        if splited[0] not in variables:
            variables[splited[0]] = 0
        if splited[1] == "dec":
            variables[splited[0]]-=int(splited[2])
        else:
            variables[splited[0]]+=int(splited[2])
    else:
        continue

print(variables[max(variables,key=variables.get)])
