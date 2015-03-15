import socket
import sys
import threading
import clientthread
import crossdomain

HOST = '';
PORT = 9991;

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('SOCket created')

try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print ( 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print( 'Socket Bind Complete')

s.listen(10)


print('Socket now listening')

while 1:
    conn, addr = s.accept()
    print  ('Connected with ' + addr[0] + ':' + str(addr[1]))
    client = clientthread.OneClient(conn);
    client.start();
    
s.close()
