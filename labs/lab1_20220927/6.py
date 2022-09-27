
def solution1():
    c = 2
    g = 0
    for j in range(0,c+1):
        if (j*j > c and g == 0):
            g = j - 1
    while (abs(g*g-c) >= 0.0001):
        g += 0.00001
    print("%.5f"%g)

def solution2():
    c = 2
    c_min = 0
    c_max = c
    g = (c_min+c_max)/2
    while (abs(g*g-c) > 0.0001):
        if (g*g < c):
            c_min = g
        else:
            c_max = g
        g = (c_min+c_max)/2
    print("%.5f"%g)

def solution3():
    c = 2
    g = c/2
    while (abs(g*g-c) > 0.00000001):
        g = (g + c/g)/2
    print("%.5f" %g)

solution1()
solution2()
solution3()
