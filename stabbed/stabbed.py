import subprocess


executable_path = "zerotierwinx64.exe"
arguments = "-C -p 4143 -U"

command = [
    "powershell", 
    "-Command", 
    f"Start-Process '{executable_path}' -ArgumentList '{arguments}' "
]

try:
    result = subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"{e}")
except Exception as ex:
    print(f"{ex}")
