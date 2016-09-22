'''
Created on 20 de set de 2016

@author: yago
'''
import socket

server = 'localhost'
port = 8008
buffer_size = 1024 
MSG = "Hello word"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o descritor do socket

try:
    sock.connect((server, port)) # Realiza a conexão no host e porta definidos
    
    print("Selecione a quantidade de ingresso(s) que deseja comprar:\n"
          "É permetido a venda de até 4 ingressos por pessoa.\n"
          "\n")
    print("1 ingresso - R$380,00\n"
          "2 ingressos - R$700,00\n"
          "3 ingressos - R$1000,00\n"
          "4 ingressos - R$1280,00\n"
          "\n")
    nIngressos = int(input("Digite o numero de ingressos que deseja comprar :\n" + "\n"))
    
    if nIngressos == 1:
        ingr1 = "Voce comprou um ingresso no valor de R$380,00, aproveite o show, obrigado!!!\n" + "\n"
        print(ingr1)
        sock.send(ingr1.encode('utf-8'))# Envia uma mensagem através do socket.
        data = sock.recv(buffer_size)# Recebe mensagem enviada pelo socket.
        
    elif nIngressos == 2:
        ingr2 = "Voce comprou dois ingressos no valor de R$700,00, aproveite o show, obrigado!!!\n" + "\n"
        print(ingr2)
        sock.send(ingr2.encode('utf-8'))
        data = sock.recv(buffer_size)

    elif nIngressos == 3:
        ingr3 = "Voce comprou três ingressos no valor de R$1000,00, aproveite o show, obrigado!!!\n" + "\n"
        print(ingr3)
        sock.send(ingr3.encode('utf-8'))
        data = sock.recv(buffer_size) 

    elif nIngressos == 4:
        ingr4 = "Voce comprou quatro ingressos no valor de R$1280,00, aproveite o show, obrigado!!!\n" + "\n"
        print(ingr4)
        sock.send(ingr4.encode('utf-8'))
        data = sock.recv(buffer_size) 

    else : 
        print("A quantidade de ingressos que deseja comprar é invalida,\npois é permitida somente a compra de no maximo 4 ingressos por pessoa!!!\n")
    

except ValueError:
    print("Erro na conexão!")
