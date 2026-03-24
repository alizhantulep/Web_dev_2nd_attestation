a = int(input())
b = int(input())

if (b % 2 == 0):
    b=b+1
for i in range(a,b):
    if(i %2 == 0):
        print(i, end=' ')