import zmq
from constCS import * #-
context = zmq.Context()

p1 = "tcp://172.31.93.112:2345" # how and where to connect
s  = context.socket(zmq.REQ)    # create request socket

s.connect(p1)                   # block until connected
s.send("Hello world p1")           # send message
message = s.recv()              # block until response
print message                   # print result
s.send("Hello world p2")           # send message
message = s.recv()              # block until response
print message                   # print result
s.send("Hello world p3")           # send message
message = s.recv()              # block until response
print message                   # print result
s.send("STOP")                  # tell server to stop
print message                   # print result
