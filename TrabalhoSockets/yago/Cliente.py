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
    print("To send >>>"+ MSG)
    sock.send(MSG.encode('utf-8')) # Envia uma mensagem através do socket.
    data = sock.recv(buffer_size) # Recebe mensagem enviada pelo socket.
    if len(str(data)) >= 0:
        print("Receive from server: "+data.decode('utf-8'))
    else:
        print("No data received from server...")
except ValueError:
    print("Erro connect!")
