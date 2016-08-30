'''
Created on 26 de ago de 2016

@author: yago
'''
a = [1,1,2,3,4,5,6]
print(len(a))# o len conta quantos elementos eu tenho em uma determinada lista


lista = []

num = int(input("Digite um número : "))

while num != 0:
    lista.append(num)
    num = int(input("Digite um número: "))

elemento = int(input("Digite o elemento a ser procurado: "))


print("O elemento %i aparece %i vezes na sequência."%(elemento, lista.count(elemento)))
        
        #o  count conta quantos elementos x tem em uma lista
