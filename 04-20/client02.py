from socket  import *
from constCS import * #-
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Exemplos de sockets')
# Required positional argument
parser.add_argument('msg', type=int,
                    help='Tipo de mensagem a ser enviada')
args = parser.parse_args()

if args.msg == 1:
    mensagem = 'EnvioProtocoloA'
elif args.msg == 2:
    mensagem = 'EnvioProtocoloB'
elif args.msg == 3:
    mensagem = 'EnvioProtocoloC'
else:
    mensagem = 'MsgAleatoria'
    # parser.error("Tipo de mensagem invalido")
    # exit

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)import argparse
s.send(mensagem)  # send same data
data = s.recv(1024)     # receive the response
print data              # print the result
s.close()               # close the connection
