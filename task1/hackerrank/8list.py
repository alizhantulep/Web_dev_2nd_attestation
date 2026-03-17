a = []

n = int(input())
for i in range(n):
    s = str(input())
    w = float(input())
    a.append([s,w])


lowest = 9999999999
for i in range (n):
    if(a[i][1] < lowest):
        lowest = a[i][1]

sec_lowest= 99999999
for i in range(n):
    if(a[i][1] < sec_lowest and a[i][1] != lowest):
        sec_lowest = a[i][1]

neww = []
for i in range(n):
    if (a[i][1] == sec_lowest):
        neww.append(a[i][0])
    
neww.sort()
for i in neww:
    print(i)