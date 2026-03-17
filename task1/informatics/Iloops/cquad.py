a=int(input())
b= int(input())

for i in range(a,b):
    for j in range(1,i):
        if (j * j == i):
            print(i)