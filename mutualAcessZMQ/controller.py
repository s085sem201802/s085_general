import zmq
import time
from Queue import Queue
# from constCS import * #-

HOST = "172.31.11.74"
PORT1 = "2345" 
p1 = "tcp://"+ HOST +":"+ PORT1 # how and where to connect

context = zmq.Context()
s = context.socket(zmq.ROUTER)    # create reply socket
s.bind(p1)                      # bind socket to address

q = Queue()
inuse = 0

while True:
    ident, msg = s.recv_multipart()
    #print('Mensagem recebida de %s: %s' % (ident, msg))

    if "REQUEST" in msg:
        print "REQUEST recebido de " + ident
        if (inuse == 0):
            inuse = ident
            s.send_multipart([ident, "OK"])
            print "** Em uso por " + ident

        else:
            q.put([ident, msg])
            print "Request adicionado na fila: " + ident

    elif "RELEASE" in msg:
        print "RELEASE recebido de " + ident
        if (not q.empty()):
            rec = q.get()
            #TODO: popular o inuse com novo ident do rec[0]
            print "Enviando OK para " + rec[0]
            s.send_multipart([rec[0], "OK"])
            print "** Em uso por " + rec[0]

        else:
            inuse = 0
            print "Recurso liberado"

    time.sleep(1)

s.close()
context.term()
