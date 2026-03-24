a = int(input())
c = list(map(int,input().split()))

for i in range(0,len(c)//2):
    temp = c[-i-1]
    c[-i-1] = c[i]
    c[i] = temp

for i in c:
    print(i, end=' ')