#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario o radio e altura dun cilindro nesta orde e calcula o seu volume. Mostra o resultado por pantalla.

radio_str = input("Introduzca o radio do cilindro: ")
altura_str = input("Introduzca a altura do cilindro: ")

radio = float(radio_str)
altura= float(altura_str)

volume = 3.1416 * radio ** 2 * altura

print("O seu volume é: ", volume)