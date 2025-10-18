#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida que calcule o valor do seguinte polinomio 2x^2 + 5x - 3 para o valor de x que especifique o usuario por teclado. Mostra o resultado por pantalla.

x_str = input("Introduza o valor de x: ")

x = float(x_str)

polinomio = 2 * x ** 2 + 5 * x - 3

print("O resultado é: ", polinomio)