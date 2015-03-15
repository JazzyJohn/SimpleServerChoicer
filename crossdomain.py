import socket
import threading

class CrossDomain(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
     
    def run(self):
        HOST = '';
        PORT = 843;

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        print ('SOCket created')

        try:
            s.bind((HOST,PORT))
        except socket.error as msg:
            print ( 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])


        s.listen(10)

        while 1:
            conn, addr = s.accept()
            while True:

                data = conn.recv(1024)
                print(data)
                if not data:
                    break;
                conn.sendall(bytes('<?xml version="1.0"?><cross-domain-policy><allow-access-from domain="*"/></cross-domain-policy>',"UTF-8"))

           
            conn.close();
            print("CrossDomainSended AllOk")
        s.close();
        
anotherSocket = CrossDomain();
anotherSocket.start();
