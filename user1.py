import socket
import threading

# HOST = "10.0.2.15"  
HOST = "127.0.0.1"  
PORT = 6666  


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # name = input()
    # s.send(name.encode("ascii")) 
    

    def recieving():
        while True:
            data_chunk = s.recv(1024)
            if data_chunk:
                print(data_chunk)
                
    def send():
        out = input()
        s.send(out.encode("ascii"))
        return out 
    
    
    rec_thread = threading.Thread(target=recieving)
    rec_thread.start()
    
    while True:
        if send() == "exit":
            s.close()