a = int(input())
count = 0
while count<=a:
    if (pow(2,count)<a):
        print(pow(2,count), end = ' ')
    count=count+1