import socket

remoteServer = input("ENTER A REMOTE HOST TO SCAN: ")

for port in range(78,85):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServer, port))
    if result == 0:
        print("PORT {}:OPEN".format(port))
    else:
        print("PORT {}:CLOSED".format(port))
    sock.close()