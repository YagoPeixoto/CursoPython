'''
Created on 25 de ago de 2016

@author: yago
'''
"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
lista=[]

for i in range(1,5):
    nota = float(input("Digite a %dª nota :"%i))
    lista.append(nota)
    
print("suas notas são:",lista)

media = (lista[0]+lista[1]+lista[2]+lista[3])/4

print("Sua media é:", media)