a = int(input())
b = list(map(int, input().split()))
count=0
prev = b[0]
for i in b:
    if (i >prev ):
        count += 1
    prev = i
print(count)