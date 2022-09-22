#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)

        print("Listening...")
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
           
            #recieve data, wait a bit, then send it back
            

            p = Process(target=multi_echo,args=(conn,addr))
            p.daemon = True
            p.start()
            print("starting process ", p)

def multi_echo(conn,addr):
    print("Connected by", addr)

    full_data= conn.recv(BUFFER_SIZE)
    
    time.sleep(0.5)
    conn.sendall(full_data)
    
    conn.shutdown(socket.SHUT_WR)
    conn.close()
    


if __name__ == "__main__":
    main()
