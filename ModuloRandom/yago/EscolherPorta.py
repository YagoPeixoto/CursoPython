'''
Created on 24 de ago de 2016

@author: yago
'''
"""
Escreva um programa para simular o jogo das portas. Faça um programa que tenha
a saída como a seguinte:
 
Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!
Escolha uma porta: 3
Você escolheu a porta 3, mas
eu lhe informo que na porta 2 há um bode.
Deseja trocar de porta (1 - Sim/ 0 - Não): 1
Ganhou um carro!
"""
import random
 
porta = int(input("Escolha uma porta entre 1, 2 e 3 para comcorrer um carro : "))
premio = random.randint(1, 3)
 
if premio != 1 and porta != 1:
    bode = 1
elif premio != 2 and porta != 2:
    bode = 2
else:
    bode = 3
 
print("A porta escolhida foi a porta %i"%porta)
print("A porta %i tem um bode!!!"%bode)
 
decisao = int(input("Você quer trocar de porta (1 - Sim or 0 - Não): "))
 
if decisao == 1:
    if porta != 1 and bode != 1:
        porta = 1
    elif porta != 2 and bode != 2:
        porta = 2
    else:
        porta = 3
 
if porta == premio:
    print("Ganhou um carro!")
else:
    print("Ganhou um bode!")