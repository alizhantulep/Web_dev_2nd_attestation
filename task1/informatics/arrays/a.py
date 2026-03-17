a = int(input())
b=[]
for i in range(a):
    b.append(int(input()))
for i in range(0,len(b),2):
    print(b[i], end= ' ')