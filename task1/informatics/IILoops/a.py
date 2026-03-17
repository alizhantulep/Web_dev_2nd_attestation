a = int(input())

count = 1
while count<=a:
    if (count*count <= a):
        print(count*count)
        count=count+1
    else:
        count=a+1