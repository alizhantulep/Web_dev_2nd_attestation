a =int(input())
b = int(input())
a = abs(a)
b = abs(b)
lena = 0, lenb = 0
newa = str(a)
for i in range(newa):
    if (newa[i] == 1):
        lena= lena+1
    else:
        lenb = lenb+1
lenq = 0, lens=0
newb = str(b)
for i in range(newb):
    if (newb[i]==1):
        lenq = lenq+1
    else:
        lens=lens+1