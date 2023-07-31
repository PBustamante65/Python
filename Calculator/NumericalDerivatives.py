import math

def f1 (x):
    h = 1E-10
    derivative = (math.pow(x + h, 2) - math.pow(x - h, 2)) / (2 * h)
    return derivative

print(f1(2))

