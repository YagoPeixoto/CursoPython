'''
Created on 15 de set de 2016

@author: yago
'''
def incrementar():
    global X
    incremento = 5  # variável local
    X += incremento  # cópia do valor de x

X = 10

incrementar()

print(X)
