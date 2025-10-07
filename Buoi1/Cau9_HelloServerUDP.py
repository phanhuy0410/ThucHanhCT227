import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print("Server đang chạy và lắng nghe trên cổng 999...")
while True:
    data, (addr, p) = s.recvfrom(1024)
    print("Đã nhận kết nối từ: ", addr)
    print("Client gửi: ",data.decode('utf-8'))
    msg = "Server: Hello client "+addr
    s.sendto(msg.encode('utf-8'), (addr, p))
    s.close()
    break


