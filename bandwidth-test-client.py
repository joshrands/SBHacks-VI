# client practice code to go in security-cam.py

# import socket module 
import socket                
import pickle
  
# Create a socket object 
s = socket.socket()          
    
# Define the port on which you want to connect 
# get this before CV and ML
port = int(input("Enter port: "))
ip = input("Enter aed ip: ")

# connect to the server (change ip address to server ip) 
s.connect((ip, port)) 

# receive data from the server 
recv_data = s.recv(8096) 
print(pickle.loads(recv_data))

# send a thank you message to the client.  
s.send('Thanks'.encode())

# close the connection 
s.close()  
 
