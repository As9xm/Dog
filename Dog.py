import platform
import os
import socket
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def collect_system_info():
    system_info = {
       Fore.RED + "OS": platform.system(),
       Fore.RED + "OS Version": platform.version(),
       Fore.RED + "OS Release": platform.release(),
       Fore.BLUE + "Architecture": platform.architecture(),
       Fore.BLUE + "Machine": platform.machine(),
       Fore.BLUE + "Processor": platform.processor(),
       Fore.GREEN + "Hostname": socket.gethostname(),
       Fore.GREEN + "IP Address": socket.gethostbyname(socket.gethostname()),
       Fore.GREEN + "Python Version": platform.python_version(),
       Fore.GREEN + "Current Directory": os.getcwd(),
       Fore.GREEN + "User": os.getlogin()
    }
    return system_info

if __name__ == "__main__":
    info = collect_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")
    print("\nSystem information collected successfully.")