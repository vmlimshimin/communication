from Crypto.Cipher import AES
from Crypto import Random

import base64
import sys
import os
import socket

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def encryptText(msg, Key):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(Key,AES.MODE_CBC,iv)
    encryptedText = cipher.encrypt(pad(msg))
    encodedText = base64.b64encode(iv + encryptedText)

    #encodedMSG = base64.b64encode(cipherText)
    #print(encodedMSG)
    #iv = encodedMSG[:16]
    #print(iv)
    #secret_key = bytes(str(Key), encoding = "utf8")
    #secret_key = base64.b64decode(Key)
    #cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    #encryptedText = cipher.encrypt(encodedMSG[16:]).strip()
    #encryptedTextStr = encryptedText.encode('utf8')

    return encodedText

print ("Enter Host IP Address: ")
HOST = sys.stdin.readline().strip()
print ("Enter Port No.: ")
PORT = int(sys.stdin.readline().strip())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("test")
while (1):
    print("Enter string: ")
    #lineStr = "Hello World 1234"
    lineStr = sys.stdin.readline().strip()
    if lineStr == "logout": break
    #line = lineStr.encode('utf8')
    secret_key = '1234567887654321'
    print("test 1")
    encodedLine = encryptText(lineStr, secret_key)
    s.sendall(encodedLine)
    print("test 2")
    data = s.recv(1024)
s.close()
print ("Received"), repr(data)