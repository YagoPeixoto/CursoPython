'''
Created on 23 de set de 2016

@author: yago
'''
matriz = []
numLinhas = int(input("Digite o numero de linhas da matriz : "))
numColunas = int(input("Digite o numero de colunas da matriz : "))

def constroiMatriz(numLinhas, numColunas, matriz):
    for i in range(1, numLinhas+1):
        linha = []
        for j in range(1, numColunas+1):
            x = int(input("Digite o elemento %i%i da matriz:" %(i,j)))
            linha.append(x)
        
        matriz.append(linha)
constroiMatriz(numLinhas, numColunas, matriz)
print(matriz)
