#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario a base e altura dun triángulo nesta orde e calcular a súa área. Mostra o resultado por pantalla.

altura_str = input("Introduce a altura: ")
base_str = input("Introduce a base: ")

altura = float(altura_str)
base = float(base_str)

area = altura * base / 2
print("O area é: ", area)