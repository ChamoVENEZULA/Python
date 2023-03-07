#!/usr/local/bin/python
# coding: latin-1
import decimal
import math


def peso():
    try:
        num = float(input('ingrese su peso:  ') )
        return num
    except :
        print('digite peso valido')
        peso()

def altura():
    try:
        alt = float(input('ingrese altura:  '))
        return alt
    except :
        print('digite peso valido')
        altura()

def IMC(peso, altura):
    imc= round( peso/math.pow(altura,2),2 )
   
    print(f'Tu índice de masa corporal es donde es: {imc}')


IMC(peso(),altura())