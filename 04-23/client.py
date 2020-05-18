import zmq
from constPS import * #-

HOST = "172.31.93.112"
PORT = "2345"

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

#for i in range(5):  # Five iterations
while True:
  time = s.recv()   # receive a message 
  print time       
