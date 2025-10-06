n = int(input("Nhập số nguyên: "))
binary = ""
b = n
while b>0:
    binary = str(b%2) + binary
    b = b//2
print(f"Số {n} ở hệ nhị phân là: {binary}")