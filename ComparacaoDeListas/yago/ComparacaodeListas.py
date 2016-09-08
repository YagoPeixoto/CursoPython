'''
Created on 8 de set de 2016

@author: yago
'''
a = ([1,2,3])
b = ([3,2,1])
print(a == b) #a comparação pega o primeiro elemento de cada lista no caso b é conssiderado > do que a
b.sort()
print(a == b)# os elementos são os mesmos e usando sort agr b é == a "a"

c = ([7,8,7])
d = ([7,7,7,7])

print(d > c)# quando os primeiros elementos são iguais o python compara o segundo elemento e assim por diante

c = ([7,7,7])
d = ([7,7,7,7])

print(d > c)# o quando os elementos são iguais a lista que tem a soma de elementos maior é a maior