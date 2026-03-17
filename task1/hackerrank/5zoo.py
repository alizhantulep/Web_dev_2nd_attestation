import numpy

a, b, c = map(int, input().split())

print(numpy.zeros((a, b, c), dtype=int))
print(numpy.ones((a, b, c), dtype=int))