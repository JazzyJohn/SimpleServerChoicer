import threading
import conf
import time

class ListOfUser:
    
    def __init__(self,server):
        self.server = server
        self.count = 0
        self.users=[]
    def has(self,uid):
        return self.users.count(uid)>0
    def add(self,uid):
        self.count+=1;
        self.users.append(uid)
    def remove(self,uid):
        self.count-=1;
        self.users.remove(uid)

class ListOfServers:
    max_users= 100
    def __init__(self,servers):
        self.servers= []
        for w in servers:
            server = ListOfUser(w)
            self.servers.append(server)
    def addUser(self,uid):
        for server in self.servers:
            if server.count<self.max_users:
                server.add(uid)
                return server
                print('ps')
        return None
    def addTo(self,uid,serverName):
        for server in self.servers:
            if server.server == serverName:
                server.add(uid)
                return True
        return False
    def whereUser(self,uid):
        for server in self.servers:
            if server.has(uid):
                return server.server
        return "notFound"
    def get(self,serverName):
        for server in self.servers:
            if server.server == serverName:
                return server
        return None
    
Servers = ListOfServers(["164.138.31.28","164.138.31.29"])

class Monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
     
    def run(self):
        while True:
            for server in Servers.servers:
                print(server.server+" "+  str(server.count))
            time.sleep(conf.monitorDelay)


anotherSocket = Monitor()
anotherSocket.start()
