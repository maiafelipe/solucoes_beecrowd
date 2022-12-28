# -*- coding: utf-8 -*-

nome = input()
salario = float(input())
vendas = float(input())
total = salario+0.15*vendas

print("TOTAL = R$ {:.2f}".format(total))