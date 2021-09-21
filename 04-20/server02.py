from socket  import *
# from constCS import * #-

HOST = ''
PORT = 2001

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  
s.listen(1)
print "Escutando na porta " + str(PORT)

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped

  if data == "EnvioProtocoloA":
    print "Dados recebidos: " + data
    conn.send("RespostaProtocoloA")
    
  elif data == "EnvioProtocoloB":
    print "Dados recebidos: " + data
    conn.send("RespostaProtocoloB")
    
  elif data == "EnvioProtocoloC":
    print "Dados recebidos: " + data
    conn.send("RespostaProtocoloC")
    
  else: 
    print "Mensagem nao reconhecida"
    print "Dados recebidos: " + data
    conn.send("MensagemNaoReconhecida")
  
  #conn.send(str(data)+"*") # return sent data plus an "*"
conn.close()               # close the connection
