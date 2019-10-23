Number={
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
Number["FUJITSU"] = 15
Number["ALIENWARE"] = 5
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
print("Giá trị từng loại máy là:")
n=0
for k,v in Number.items():
    print(k,Number[k]*Cost[k])
    n = n +Number[k]*Cost[k]
print("Tổng giá trị các loại máy là :",n)