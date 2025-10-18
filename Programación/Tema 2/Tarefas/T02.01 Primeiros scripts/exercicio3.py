#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario dous números enteiros e multiplicalos. Mostra o resultado por pantalla.

num1_str = input("Introduce el primer número: ")
num2_str = input("Introduce el segundo número: ")

num1 = int(num1_str)
num2 = int(num2_str)

multiplicacion = num1 * num2
print("El producto es: ", multiplicacion)