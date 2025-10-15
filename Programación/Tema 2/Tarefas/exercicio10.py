#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que simule unha calculadora que reciba unha cantidade de Libras Esterlinas e realice o cambio de divisas a euros. Un € é igual a 1,10 libras. Mostra o resultado por pantalla.

libras_str = input("Introduza o valor en libras esterlinas: ")

libras = float(libras_str)

euros = libras / 1.1

print("Equivalen a: ", euros, " euros")