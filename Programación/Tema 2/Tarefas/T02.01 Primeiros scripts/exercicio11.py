#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alberto Muñoz Vazquez"

# Escribe un script que pida ao usuario primeiro o seu salario bruto e despois o IRFP en tanto por cen e indícalle o seu salario neto. Utiliza a seguinte fórmula para o calculo: salario_neto = salario_bruto - (salario_bruto * IRPF). Mostra o resultado por pantalla.

salarioBruto_str = input("Introduza o seu salario bruto: ")
irpf_str=input("Introduza a porcentaxe de IRPF: ")

salarioBruto = float(salarioBruto_str)
irpf = float(irpf_str)

salarioNeto = salarioBruto - (salarioBruto * (irpf / 100))

print("O seu salario neto é de: ", salarioNeto)