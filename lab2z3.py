from math import sqrt

print("rozwiazanie rownania w postaci ax^2+bx+c")
a = int(input("podaj wspolczynnik a: "))
b = int(input("podaj wspolczynnik b: "))
c = int(input("podaj wspolczynnik c: "))

delta = (b^2)-4*(a*c)

if delta < 0:
    print("nie da sie")
else:
    sqrtdelta=sqrt(delta)

    x1=((-1*b)-sqrtdelta)/2*a
    if delta==0:
        print("rownanie ma 1 rozwiazanie : " + x1)
    x2=((-1*b)+sqrtdelta)/2*a
    if delta > 0:
        print("rozwiazanie 1 : " + x1)
        print("rozwiazanie 2 : " + x2)