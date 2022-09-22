#!/usr/bin/env python3
import socket, sys
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def main():
    host = 'www.google.com'
    port = 80
    payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    buffer_size = 4096

    
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    #bind socket to address
    s.bind((HOST, PORT))
    #set to listening mode
    s.listen(2)
        
    #continuously listen for connections
    while True:
        conn, addr = s.accept()
        

        socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        remote_ip = get_remote_ip(host)

        socket2.connect((remote_ip,port))

        p = Process(target=multi_proxy,args=(conn,socket2,addr))

        p.daemon = True
        p.start()

        print("starting process ",p)


            
        #recieve data, wait a bit, then send it back
       
    conn.close()

def multi_proxy(conn,socket2,addr):
    print("Connected by ",addr)

    full_data = conn.recv(BUFFER_SIZE)

    socket2.sendall(full_data)

    socket2.shutdown(socket.SHUT_WR)

    data=socket2.recv(BUFFER_SIZE)

    conn.send(data)

    conn.close()

    



if __name__ == "__main__":
    main()