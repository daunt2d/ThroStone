import socket

# ThroStone by Reonized open release 1.0
# utilizes GNU General Public License (GPL)
# DO NOT UTILIZE THROSTONE FOR ILLEGAL ACTIVITIES! by the Developers at Reonized LLC

while True:
    # create the socket object and wait for the user to enter the destination IP and port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("ThroStone by Reonized.\n")
    ip = input("Enter Valid IP Address: ")
    port = int(input("IP Port: "))
    s.connect((ip, port))
    s.sendall(b"data")
    print("sending data to: " + ip)
