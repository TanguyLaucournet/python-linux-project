# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
# get host name , address and info
a =socket.gethostname()
print("host: "+a)

b =socket.gethostbyname(a)
print('addr: '+b)

c=socket.gethostbyaddr(b)
print(c)

# receive data from the server 
print(s.recv(1024))
# close the connection 
s.close()  