#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario o radio dunha circunferencia e calcular o seu perímetro e área. Mostra o resultado por pantalla, primeiro o perímetro e despois a área.

radio_str = input("Introduza o radio da circunferencia: ")

radio = float(radio_str)

perimetro = 2 * 3.1416 * radio
area = 3.1416 * radio ** 2

print("O seu perímetro é de: ", perimetro)
print("A súa área é de: ", area)