a = int(input())
s = 0
count = a
while s == 0:
    q = count
    while q>1 and q % 2 == 0:
        q=q//2
    if q== 1:
        s = 1
        print(count)
    count=count+1