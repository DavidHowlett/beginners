import math

"""def pow(x,y):
    return x**y

def fact(x):
    assert type(x)==int
    factorial=1
    while x>0:
        factorial*=x
        x-=1
        return(factorial)
    
def fact2(x):
    assert type(x)==int
    return 1 if x<2 else x*fact2(x-1)
    
for i in range(10):
    print(i,fact2(i))"""


def integral(ind, x1, x2):
    if ind == -1:
        return math.log(x2) - math.log(x1)
    y = x2 ** (ind + 1) / (ind + 1)
    y -= x1 ** (ind + 1) / (ind + 1)
    return y


print(integral(-1, 7, 10))
