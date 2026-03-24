x,y = map(int, input().split())

if (x==1):
    boolx = True
else:
    boolx= False
if(y==1):
    booly =True
else:
    booly= False

def xor(x,y):
    if (x==True and y==True):
        print(x,y)
        return False
    elif(x==True or y==True):
        return True
    else:
        return False
    

print(xor(boolx,booly))