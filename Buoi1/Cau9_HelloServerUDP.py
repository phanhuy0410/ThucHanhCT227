import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
while True:
    data, (addr, p) = s.recvfrom(1024)
    print("Đã nhận kết nối từ: ", addr)
    msg = "Hello client "+addr
    s.sendto(msg.encode('utf-8'), (addr, p))


