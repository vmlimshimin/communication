import socket

HOST = '172.23.197.178'
#HOST = '137.132.228.45'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("test")
line = "Hello World"
line = line.encode()
s.sendall(line)
data = s.recv(1024)
s.close()
print ("Received"), repr(data)
            