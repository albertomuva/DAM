#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario dous números enteiros e realiza a división do primeiro número entre o segundo e mostra o resto da división por pantalla.

num1_str = input("Introduce o primero número: ")
num2_str = input("Introduce o segundo número: ")

num1 = int(num1_str)
num2 = int(num2_str)

resto = num1 % num2
print("O resto é: ", resto)