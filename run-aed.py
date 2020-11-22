# Run this script on the autonomous AED system. 
# It will wait for information from the security cam before being dispatched 

# Step 1: Create network socket and wait for dispatch signal 
# first of all import the socket library 
import socket
import random            

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/home/pi/SBHacks-VI/Autonomy/CarStuff')

from FinalAED import *

# next create a socket object 
s = socket.socket()          

port = 1234#int(input("Enter your port: "))
ip = "169.231.174.238"#raw_input("Enter your ip: ")
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind((ip, port))         
print("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening") 
  
# a forever loop until we interrupt it or  
# an error occurs 
  
# Establish connection with client. 
c, addr = s.accept()      
print('Got connection from', addr) 
  
# send a thank you message to the client.  
c.send('Thank you for connecting'.encode()) 

# receive data from system
data = c.recv(1024)
print(data) 

# Close the connection with the client 
c.close()

if (data == b'GO'):
    print("Gametime bitch")
	# execute drive-test-V3
    deployAEDSystem()
