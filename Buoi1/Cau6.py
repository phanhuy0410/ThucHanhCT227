def List(list):
    so_lon_nhat = max(list)
    tong = sum(list)
    tich = 1
    for i in list:
        tich*=i
    return so_lon_nhat, tong, tich
ds = [5,7,3,9,10]
lon_nhat, tong, tich = List(ds)
print("Danh sách: ",ds)
print("Số lớn nhất = ",lon_nhat)
print("Tổng = ",tong)
print("Tích = ",tich)