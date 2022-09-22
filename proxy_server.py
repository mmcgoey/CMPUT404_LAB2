#!/usr/bin/env python3
import socket, sys
import time

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
   

    
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    #bind socket to address
    s.bind((HOST, PORT))
    #set to listening mode
    s.listen(2)
        
    #continuously listen for connections
    while True:
        conn, addr = s.accept()
        print("Connected by", addr)

        socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        remote_ip = get_remote_ip(host)

        socket2.connect((remote_ip,port))

        full_data = conn.recv(BUFFER_SIZE)


        socket2.sendall(full_data)

        socket2.shutdown(socket.SHUT_WR)

        data=socket2.recv(BUFFER_SIZE)

        conn.send(data)

        conn.close()

        
        
            
        
       
    conn.close()


if __name__ == "__main__":
    main()