import math
def resta(n1, d1, n2, d2):
    n3 = n1 * d2 - d1 * n2
    d3 = d1 * d2
    mcd = math.gcd(n3, d3)
    n3 //= mcd
    d3 //= mcd

    return n3, d3


def restaMal(n1, d1, n2, d2):
    n3 = n1 - n2
    d3 = d1 - d2
    mcd = math.gcd(n3, d3)
    n3 //= mcd
    d3 //= mcd
    if (n1 > d1 or (mcd == 1 and n3 == -1 and d3 < 0)):
        n3 = int(math.fabs(n3))
        d3 = int(math.fabs(d3))
    return n3, d3


linea = input()
while linea != "0 0":
    datos = linea.strip().split(' ')
    b = int(datos[0])
    n = int(datos[1])
    x = ""
    for a in range(10):
        for m in range(1,30):
            if(a != b and b != m):
                val1 = resta(a, m, b, n)
                val2 = restaMal(a, m, b, n)
                if (val1 == val2):
                    x += str(a)+"/"+str(m) + " "
    print(x)
    linea = input()
