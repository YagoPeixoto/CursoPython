'''
Created on 25 de ago de 2016

@author: yago
'''
lista = [1,2,3,4, [4,56,77,65]]
print(lista[4])#imprime a lista dentro da lista
print(lista[4][2])#imprime a um valor da lsta dentro de outra lista

lista = [1,2,[23,13,[12,14]],[3,44,66]]
print(lista)    
print(lista[3][1])   
print(lista[2])
print(lista[2][2][1])#deve imprimir 14