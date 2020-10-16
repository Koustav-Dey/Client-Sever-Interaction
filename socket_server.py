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


print(bcolors.BOLD + bcolors.RED + bcolors.UNDERLINE +
      "\n\n\t  SERVER ! " + bcolors.ENDC)
print(bcolors.BOLD + bcolors.YELLOW +
      "\t==============" + bcolors.ENDC)  

#IPV4,TCP
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Change Ip and Port for remote Connection
server_socket.bind(('127.0.0.1',5090))

#Passive : How many connection You want to hold
server_socket.listen(10)
print(bcolors.BLUE + "\n\n[+] Listening for connections on 127.0.0.1:5090... " + bcolors.ENDC)

while(True):

    conn, addr = server_socket.accept()
    print(bcolors.MEGNATA + "\n[+] Got a connection from {}".format(addr))

    while True:

        data = conn.recv(2048)

        #Break the Connection
        if(data.decode() == 'bye'): 
            break

        print("\n[+]Waiting For CLEINT @ Responce....")
        print(bcolors.GREEN + "\n[+]Waiting ", end="")
        list1 = [".", ".", ".", ".", ".", ".", ".", "."]
        for i in (list1):

            print(f"{i}", end="")
            time.sleep(1)
        
        print(bcolors.MEGNATA + "\n\n[+] Client sent :",data.decode())

        server_data = input(bcolors.YELLOW + "\nEnter SERVER ! Reply : " + bcolors.ENDC)
        conn.send(server_data.encode())
        print(bcolors.GREEN)
        print("\n[+]Your Data Will Be Sent ! ")

    conn.close()
    print(bcolors.RED + "\n[+]Client Disconnected !" + bcolors.ENDC)

