def until(n):
    suv = ""
    for i in range (1,n+1):
        suv = suv+str(i) 
    return suv
        
n = int(input())
print(until(n))