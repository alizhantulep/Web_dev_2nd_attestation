a = int(input())

count = 0
c=0
while count<=a:
    if(pow(2,count) ==a):
        print("YES")
        c=1
    count=count+1
if(c==0):
    print("NO")