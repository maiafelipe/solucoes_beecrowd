# -*- coding: utf-8 -*-

PI = 3.14159

a, b, c = (float(s) for s in input().split())
aTriangulo = (a*c)/2
aCirculo = c * c * PI
aTrapezio = ((a+b)/2)*c
aQuadrado = b*b
aRetangulo = a*b

print("TRIANGULO: {:.3f}".format(aTriangulo))
print("CIRCULO: {:.3f}".format(aCirculo))
print("TRAPEZIO: {:.3f}".format(aTrapezio))
print("QUADRADO: {:.3f}".format(aQuadrado))
print("RETANGULO: {:.3f}".format(aRetangulo))

"""
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
"""