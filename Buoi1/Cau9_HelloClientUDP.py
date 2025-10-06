import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hi server!"
s.sendto(msg.encode('utf-8'), ('127.0.0.1', 9999))
data, (addr, p) = s.recvfrom(1024)
print(data.decode('utf-8'))
s.close