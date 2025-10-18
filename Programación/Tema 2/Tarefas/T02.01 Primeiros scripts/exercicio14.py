#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario o radio dunha esfera e calcula o seu volume. Mostra o resultado por pantalla.

radio_str = input("Introduza o radio da esfera: ")

radio = float(radio_str)

volume = 4 / 3 * 3.1416 * radio ** 3

print("O seu volume é: ", volume)