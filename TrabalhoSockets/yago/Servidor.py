'''
Created on 20 de set de 2016

@author: yago
'''
import socket

tamanhoBuffer = 1024
msgServer= "Hello, comunicação extabelecida..."
host = 'localhost' 
porta = 8008


def create_server():#função para criar o server

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o descritor do socket
    
    sock.bind((host, porta)) # Associa o endereço e porta ao descritor do socket.
    sock.listen(10) # Tamanho maximo da fila de conexões pendentes

    print("Server iniciado na porta 8008...")

    while True:
        try:
            (con, address) = sock.accept() # aceita conexoes e recupera o endereco do cliente.
            print(address[0]+" Conectando...")
            data = con.recv(tamanhoBuffer) # Recebe uma mensagem do tamanho tamanhoBuffer
            if len(str(data)) >= 0:
                print(address[0]+" say: " + data.decode('UTF-8'))
                print("Response: " + msgServer)
                con.send(msgServer.encode('utf-8')) # Envia mensagem através do socket.

            else:
                print("Dados não recebidos: "+address[0])
        except ValueError:
            print("Erro")


if __name__== "__main__":
    create_server()# chama a função criada
