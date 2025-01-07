import socket
import os

HOST = '127.0.0.1'
PORT = 52525

def receive_files(server_socket):
    conn, addr = server_socket.accept()
    print(f"CONNECTION FROM {addr}")
    
    while True:
        try: 
            file_name = conn.recv(1024).decode()
            if not file_name: break
            print(f"{file_name}")
        except:pass

        try: 
            file_size = int(conn.recv(1024).decode())
            print(f"SIZE: {file_size}")
        except:pass
        
        with open(f"received\\{file_name}", 'wb') as file:
            received_bytes = 0
            while received_bytes < file_size:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
                received_bytes += len(data)
                print(f"RECEIVING {received_bytes}/{file_size}", end='\r')
        
        print(f"\n{file_name} RECEIVED")
    
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"LISTENING... {HOST}:{PORT}")
        while True:
            receive_files(server_socket)

if __name__ == '__main__':
    main()
