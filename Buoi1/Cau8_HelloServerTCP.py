import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(1)
print("Server đang chạy và lắng nghe trên cổng 999...")
while True:
    cli, (remote_host, remote_port) = s.accept()
    print("Đã nhận kết nối từ: ", remote_host)
    msg = "Server: Hello client "+remote_host
    cli.send(msg.encode('utf-8'))
    cli_msg = cli.recv(1024).decode('utf-8')
    print("Nhận từ client: ",cli_msg)
    cli.close()
    break
