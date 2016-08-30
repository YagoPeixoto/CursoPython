'''
Created on 30 de ago de 2016

@author: yago
'''
"""
Escreva um programa que crie uma lista de elementos, até se entrar -1,
e depois imprima todos os números da lista que são maiores que 10.
"""
lista = []

num = int(input("Digite um valor :"))
while num != -1:
    lista.append(num)
    num = int(input("Digite um valor :"))
    
print ("Os numeros maiores que 10 são : ")
for i in lista: #percorre a lista selecionada
    if i > 10:# i percorre cada valor da lista e passa a ter o valor do numero percorrido por cada ciclo for
        print (i)