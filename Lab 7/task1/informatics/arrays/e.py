a = int(input())
b = list(map(int, input().split()))
bol = False
i = 0
c = 1
while bol ==False:
    if (b[i] > 0 and b[c] > 0):
        bol = True
    elif (b[i] < 0 and b[c] < 0):
        bol = True
    else:
        i += 1
        c +=1
    if (c == len(b)):
        break
if (bol):
    print("YES")
else:
    print("NO")