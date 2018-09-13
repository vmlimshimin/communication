import serial
import socket

ser = serial.Serial("/dev/ttyAMA0",9600)
ser.flushInput()


HOST = '172.23.197.178'
#HOST = '137.132.228.45'
PORT = 8890
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
#print("test")
#line = "Hello World"
#line = line.encode()
#s.sendall(line)
#data = s.recv(1024)
#s.close()
#print ("Received"), repr(data)

while True:
        #print("Johnny chan")
        read_serial= ser.readline()
        #line = read_serial.encode()
        s.sendall(read_serial)
        data = s.recv(1024)
        #print(read_serial)
s.close()