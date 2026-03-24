a = int(input())
b = []
for i in range(a):
    command = input().split()
    if (command[0] == "insert"):
        b.insert(int(command[1]),int(command[2]))
    elif (command[0] == "append"):
        b.append(int(command[1]))
    elif(command[0]=="remove"):
        b.remove(int(command[1]))
    elif(command[0]=="print"):
        print(b)
    elif (command[0]=="sort"):
        b.sort()
    elif(command[0]=="reverse"):
        b.reverse()
    elif(command[0]=="pop"):
        b.pop()
    