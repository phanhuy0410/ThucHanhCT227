import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(1)
while True:
    cli, (remote_host, remote_port) = s.accept()
    print("Đã nhận kết nối từ: ", remote_host)
    msg = "Hello client "+remote_host
    cli.send(msg.encode('utf-8'))
    cli.close
