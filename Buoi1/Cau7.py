import socket
print("Tên máy cục bộ: ",socket.gethostname())
print("Địa chỉ IP của www.ctu.edu.vn: ",socket.gethostbyname("www.ctu.edu.vn"))
print("Tên máy tính của 123.30.143.225: ",socket.gethostbyaddr("123.30.143.225"))