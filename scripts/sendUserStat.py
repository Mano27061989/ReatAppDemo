import json
import re
import time
import socket

IPADDR = '127.0.0.1'
PORTNUM = 20000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
s.connect((IPADDR, PORTNUM))

with open("/var/log/httpry/enp0s3.log") as file:

    while True:
      linePtr =file.readlines()
      for line in linePtr:
         field = line.split()
         if re.search(r'2018',field[0]):
           userstat = {}
           userstat["userIp"] = field[3]
           userstat["destIp"] = field[2]
           userstat["timeStamp"] = field[0] +" "+ field[1]
           userstat["status"] = field[9]
           jsonOp  = json.dumps(userstat)
           print jsonOp
           try:        
             s.send(jsonOp)
           except:
             print "Socket Error.."
         else:
           continue
    time.sleep(0.5)   

s.close()

