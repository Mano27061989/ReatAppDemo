import sys
import subprocess
from operator import truediv
import json
import re
import time
import socket

IPADDR = '127.0.0.1'
PORTNUM = 10000

while True:
 cmd="free -m |grep 'Mem'|awk '{print $2,$3}'"
 out = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
 
 stdout,stderr = out.communicate()
 
 mem_stat = stdout.split()
 
 total_mem = mem_stat[0]
 used_mem  = mem_stat[1]
 
 
 total_percent_mem_used= truediv(int(used_mem), int(total_mem)) * 100
 
 total_percent_mem_used=str(round(total_percent_mem_used,2))
 
 #print(total_percent_mem_used)
 
 cpu_cmd="mpstat |tail -n 1|awk '{print $13}'"
 cpu_out = subprocess.Popen(cpu_cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
 
 stdout2,stderr2 = cpu_out.communicate()
 
 idle_cpu = stdout2
 total_percent_cpu_used= 100 - float(idle_cpu)
 
 total_percent_cpu_used=str(round(total_percent_cpu_used, 2))
 #print(total_percent_cpu_used)
 
 
 free_disk_cmd="df -h |grep  sda1|head -n 1|awk '{print $5}'"
 
 free_disk_out = subprocess.Popen(free_disk_cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
 
 stdout3,stderr3 = free_disk_out.communicate()
 
 free_disk_space=stdout3.replace('%','')
 
 #print(free_disk_space)
 
 
 
 s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
 s.connect((IPADDR, PORTNUM))
 
 
 sysstat = {}
 sysstat["cpu"] =  total_percent_cpu_used
 sysstat["mem"] =  total_percent_mem_used
 sysstat["disk"] =  free_disk_space
 jsonOp  = json.dumps(sysstat)
 print jsonOp
 try:
      s.send(jsonOp)
 except:
      print "Socket Error.."
      s.close()
 
 time.sleep(1)
#print(sysstat)
