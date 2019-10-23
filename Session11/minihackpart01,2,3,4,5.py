Number={
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
print("Số lượng MACBOOK là:",Number["MACBOOK"])
n = input("Nhập hãng máy tính cần kiểm tra:")
print("Số lượng máy đó là:",Number[n.upper()])
Number["TOSHIBA"] = 10
print(Number)

May = input("Nhập loại máy cần thêm:")
so_luong = int(input("Nhập số lượng máy đang dược thêm:"))
Number[May.upper()] = so_luong
print(Number)

Number["DELL"] = 60
Number["MACBOOK"] = 2
print(Number)

print("Số lượng MACBOOK có trong kho là :",Number["MACBOOK"])
s=0
for v in Number.values():
    s=s+v
print("Tổng số máy là :",s)

for k,v in Number.items():
    print(k,":",v)

Number["FUJITSU"] = 15
Number["ALIENWARE"] = 5
print(Number)

x =0
for v in Number.values():
    x=x+v
print("Tổng số máy là :",x)

Cost = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000
}

print("ASUS:", Cost["ASUS"],'%')
c = input("Nhập hãng máy cần xem giá:")
print(c.upper(),':',Cost[c.upper()])

print("Giá trị đơn hàng 5 máy ASUS là:",Cost["ASUS"]*5 )
x=x-5
print("Số máy còn lại trong kho là:",x)
Number["ASUS"] = Number["ASUS"]-5
print(Number["ASUS"])

Loai = input("Nhập loại máy cần đặt: ")
soluong = int(input("Nhập số lượng máy cần đặt: "))
if soluong<=Number[Loai.upper()]:
    print("Giá trị của đơn hàng là: ",Cost[Loai.upper()]*soluong)
    x = x-soluong
    print("Số máy còn lại trong kho là:",x)
else:
    print("Số máy không đủ.")


