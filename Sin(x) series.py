from math import *
def sinx(x, n):
    x = (x*pi)/180
    a = sin(x)
    k = 0
    for i in range(n):
        sign = (-1)**i
        a = (x**((2*i)+1))/(factorial((2*i)+1)*sign)
        k += a
    return k

print(sinx(60,3))