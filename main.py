import math
from fractions import Fraction

def resta(n1, d1, n2, d2):
    n3 = n1 * d2 - d1 * n2
    d3 = d1 * d2
    return Fraction(n3, d3)

def restaMal(n1, d1, n2, d2):
    n3 = n1 - n2
    d3 = d1 - d2
    if (n1 > d1 or (n3 == -1 and d3 < 0)):
        n3 = int(math.fabs(n3))
        d3 = int(math.fabs(d3))
    return Fraction(n3, d3)

linea = input()
while linea != "0 0":
    datos = linea.strip().split(' ')
    b = int(datos[0])
    n = int(datos[1])
    listax = []
    for a in range(b):
        for m in range(1,1000000):
            if(a != b and n != m):
                val1 = resta(a, m, b, n)
                val2 = restaMal(a, m, b, n)
                if (val1 == val2):
                    listax.append((a,m))
    listax.sort(key=lambda tup: tup[1],reverse = True)
    x = ""
    for (i,j) in listax:
        x += str(i)+ "/" + str(j)+" "
    print(x[:-1])
    linea = input()
