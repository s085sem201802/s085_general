import zmq
import sys
# from constCS import * #-

if len(sys.argv) < 1:
    print "Argumentos: <MSG>. Ex: REQUEST, RELEASE"
    sys.exit()
msg = sys.argv[1] 
node = sys.argv[2]
# node = "002"

HOST = "172.31.11.74"
PORT1 = "2345"
p1 = "tcp://"+ HOST + ":" + PORT1 # how and where to connect

context = zmq.Context()
s  = context.socket(zmq.DEALER)    # create request socket
#ident = 1
ident = u'worker-%s' % node
s.identity = ident.encode('ascii') # use this if the ident is integer
s.connect(p1)                   # block until connected
print('Client %s started' % (ident))

#poll = zmq.Poller()
#poll.register(s, zmq.POLLIN)

if (msg == "REQUEST"):
    payload = (msg +" "+ node) 
    s.send_string(payload)
    print "Mensagem enviada: " + payload
    recmsg = s.recv()              # block until response
    print "Mensagem recebida: " + recmsg   
    if "OK" in recmsg:
        print "Acessando o recurso"

if (msg == "RELEASE"):
    payload = (msg +" "+ node) 
    s.send_string(payload)
    print "Mensagem enviada: " + payload

s.close()
context.term()
