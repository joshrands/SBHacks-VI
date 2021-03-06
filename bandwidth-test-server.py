# Run this script on the autonomous AED system. 
# It will wait for information from the security cam before being dispatched 

# Step 1: Create network socket and wait for dispatch signal 
# first of all import the socket library 
import socket
import random            
import pickle 

# next create a socket object 
s = socket.socket()          

port = int(input("Enter your port: "))
ip = input("Enter your ip: ")
  
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
fake_data = []
for i in range(0,8000):
	fake_data.append(255)

data = pickle.dumps(fake_data)
c.send(data) 

print(c.recv(1024))


