import socket
import os
import pty

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind(("0.0.0.0", 1337))
serv.listen()
conn, addr = serv.accept()
os.dup2(serv.fileno(),0)
os.dup2(serv.fileno(),1)
os.dup2(serv.fileno(),2)
pty.spawn("./funk32")