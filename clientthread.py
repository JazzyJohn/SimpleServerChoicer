import threading
import serverlist

class OneClient(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.uid= "";
        self.server = None
    def run(self):
    
        while True:
            try:
                data = self.conn.recv(1024)
                             
                if not data:
                    break;
                try:
                    command =data.strip().decode("UTF-8").split(" ");
                    if command[0] == "UID":
                        self.uid = command[1]
                        if self.server is None:
                            print("Connected "+self.uid)
                            self.server = serverlist.Servers.addUser(self.uid);
                        self.send(self.server.server)
                      
                    elif  command[0] == "Where?":
                        self.send(serverlist.Servers.whereUser(command[1]));
                    elif  command[0] == "Ping":
                        self.send("pong")
                    elif  command[0] == "ReconnectMe":
                        
                        if serverlist.Servers.addTo(self.uid,command[1]) :
                            self.server.remove(self.uid);
                            self.server = serverlist.Servers.get(command[1])
                            self.send("OK")
                        else :
                            self.send("NotOK")
                    else:
                        self.send("I don't no taht command sorry")
                except UnicodeDecodeError:
                    print("ERROR End")
            except ConnectionResetError:
                print("Rude Client")
                break;       


        print("Connection End "+self.uid)
        self.server.remove(self.uid);
        self.conn.close()
    def send(self,msg):
        self.conn.sendall(bytes(msg+"\r\n","UTF-8"))

  

