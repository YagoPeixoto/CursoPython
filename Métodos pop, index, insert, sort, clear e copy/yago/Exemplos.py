'''
Created on 1 de set de 2016

@author: yago



#O metodo pop remove um certo elemento da lista determinado pelo indice
a = [1,2,3,4,5,6,7]
indice = int(input("Digite o indice do elemento que será removido, lembrando que  o indice comeca no 0 : "))
a.pop(indice)
print(a)

# O metodo index revela onde esta um elemento na lista pela sua pocição no indice
b = [23,4,6,78,9,2,56]
valor = int(input("Digite o valor do a ser procurado : "))
print(b.index(valor))


#O insert insere um elemento na lista usando o valor e o indice para o elemento ser incerido
c= [3,43,6,65,23,23,76]
valor = int(input("digite um valor para ser incerido : "))
indice = int(input("Digite o indice para ser colocado o valor : "))
c.insert(indice, valor)
print(c)


#O metodo sort organiza a lista em ordem crescente
b = [23,4,6,78,9,2,56]
b.sort()
print(b)

#O metodo clear limpa a lista de modo mais eficiente que atribuir uma lista vazia 
d = [23,4,6,78,9,2,56]
print("D",d.clear())
'''

# O metodo copy copia uma lista mas não copia o endereço na memoria
k = [23,4,6,78,9,2,56]
birrl = k.copy()
print(birrl)

birrl.insert(3, 99)

print(birrl)
print(k)


