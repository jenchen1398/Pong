import threading,SocketServer,time
import struct

class requestHandler(SocketServer.StreamRequestHandler):
    #currentUserLogin={} #{clientArr:accountName}
    def handle(self):
        posvec=self.request.recv(1024)
        x,y = struct.unpack('ff', posvec)
        print('x at ' + str(x))
        print('y at ' + str(y))
        #while requestForUpdate!='':           
         #   print(posvec)
            # self.wfile.write('server reply:{0}'.format(requestForUpdate))
          #  posvect=self.request.recv(1024)
        print('client disconnect')

class broadcastServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':

    server=broadcastServer(('localhost',20000),requestHandler)
    #t = threading.Thread(target=server.serve_forever)
    #t.daemon=True
    #t.start()
    server.serve_forever()
    print('server start')
    n=0
    while n<=60:
        print(n)
        n+=1
        time.sleep(1)
    server.socket.close()



# import socket

# srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# srvsock.bind(('127.0.0.1', 23000))

# srvsock.listen(5)

#while 1:
 #    clisock, (remhost,remport) = srvsock.accept()
 #    str = clisock.recv(100)
  #   print str
#     clisock.close()
    