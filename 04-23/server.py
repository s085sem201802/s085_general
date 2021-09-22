import zmq, time
from constPS import * #-

context = zmq.Context()         
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+ HOST +":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:                    
  time.sleep(1)                    # wait every 5 seconds
  hora = time.asctime()
  print hora
  s.send("TIME " + hora) # publish the current time
