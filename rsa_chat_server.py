import socket
sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
sock.bind (('',5050))
clients = {}
print ('Start Server')
while True:
    data, addres = sock.recvfrom(1024)
    if addres not in clients:
        clients[data.split()[0]] = addres
    for client in clients:
        if data.split()[1] != b'0000000000':
            sock.sendto(data, clients[client])
    print(clients)