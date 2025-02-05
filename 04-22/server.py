import zmq
from constCS import * #-
context = zmq.Context()

p1 = "tcp://"+ HOST +":"+ PORT1 # how and where to connect
p2 = "tcp://"+ HOST +":"+ PORT2 # how and where to connect
s  = context.socket(zmq.REP)    # create reply socket

s.bind(p1)                      # bind socket to address
s.bind(p2)                      # bind socket to address
while True:
  message = s.recv()            # wait for incoming message
  if not "STOP" in str(message):     # if not to stop...
    reply = str(message.decode())+'*'
    s.send(reply.encode())       # append "*" to message
  else:                         # else...
    break                       # break out of loop and end
