n = int(input("Nhập n = "))
S = 0
for i in range(1,n+1):
    S+=i
print("Tổng S = ",S)

S1 = 0
for i1 in range(1,n+1):
    S1+=2*i1+1
print("Tổng S1 = ",S1)

S2 = 0
for i2 in range(1,n+1):
    S2+=2*i2
print("Tổng S2 = ",S2)