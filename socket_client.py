import socket
from time import time
import time

class bcolors:

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    MEGNATA = '\033[95m'


print(bcolors.BOLD + bcolors.GREEN + bcolors.UNDERLINE +
      "\n\n\t  CLIENT @ " + bcolors.ENDC)
print(bcolors.BOLD + bcolors.YELLOW +
      "\t==============" + bcolors.ENDC)    

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',5090))

while True:

    data = input(bcolors.RED + "\nEnter Your data to send : ")
    client_socket.send(data.encode())
    print(bcolors.GREEN + "\n[+]Your Data Will Be Sent " + bcolors.ENDC)

    #Received Data
    server_data = client_socket.recv(2048)

    if(server_data == ''): break
    if(data == 'bye'):
        print(bcolors.RED + "\n[+] You Are Disconnected !\n" + bcolors.ENDC)
        print("\n\n")
        break

    print(bcolors.RED + "\n[+]Waiting For SERVER ! Responce....")
    print(bcolors.GREEN + "\n[+]Waiting ", end="")
    list1 = [".", ".", ".", ".", ".", ".", ".", "."]
    for i in (list1):

        print(f"{i}", end="")
        time.sleep(1)
    print(bcolors.ENDC)
        
    print(bcolors.MEGNATA + "\n[+] Server sent : ", server_data.decode() + bcolors.ENDC)

client_socket.close() 