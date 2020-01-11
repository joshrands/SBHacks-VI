# import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
    
# Define the port on which you want to connect 
# get this before CV and ML
port = int(input("Enter port: "))
ip = "127.0.0.1"

# connect to the server (change ip address to server ip) 
s.connect((ip, port)) 

# receive data from the server 
print(s.recv(1024)) 

# send a thank you message to the client.  
s.send('Dispatch to Q2 now!'.encode())

# close the connection 
s.close()  
 
