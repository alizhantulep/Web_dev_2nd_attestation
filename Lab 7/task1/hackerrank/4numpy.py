import numpy
def arrays(arr):
    newarray = numpy.array(arr,float)[::-1]
    return newarray
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)